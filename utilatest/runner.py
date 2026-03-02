# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import functools
import importlib
import inspect
import os
import subprocess  # nosec
import sys

import pytest
import utilo

import utilotest


def run(
    cmd: str,
    cwd: str = None,
    env: dict = None,
    expect: bool = True,
    verbose: bool = False,
) -> subprocess.CompletedProcess:
    """Run external process.

    Args:
        cmd(str): command to run
        cwd(str): current working directory
        env(dict): modify environment variable for test run. If nothing is
                   passed, the global environment variable is used.
        expect(bool): if True: fail on error
                      if False: fail on success
                      if None: return completed process
        verbose(bool): log executed command and location
    Returns:
        Completed process.
    """
    cwd = cwd if cwd else os.getcwd()
    assert os.path.exists(cwd)
    msg = f'cwd {cwd} is not a valid directory'
    assert os.path.isdir(cwd), msg
    env = os.environ if env is None else env
    if verbose:
        utilo.log(f'cd {cwd}')
        utilo.log(cmd)
    # run process
    completed = subprocess.run(  # nosec, pylint:disable=subprocess-run-check
        cmd,
        cwd=cwd,
        env=env,
        errors='replace',
        shell=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )
    if expect is True:
        utilotest.assert_success(completed)
    if expect is False:  # pylint:disable=C2001
        utilotest.assert_failure(completed)
    return completed


@utilo.rename(monkeypatch='mp', success='expect')
def run_cov(
    cmd: str,
    process: str,
    main: callable,
    expect: bool,
    mp,
) -> int:
    """Run `main` with `cmd`.

    Args:
        cmd(str): command to run
        process(str): name of executed tool
        main(callable): method to run
        expect(bool): expectation that process succeeds or fails,
                      use None to skip check
        mp(fixture): pytest patch/mp feature
    Returns:
        Return code of completed process.
    """
    with contextlib.suppress(AttributeError):
        cmd = cmd.split()
    assert callable(main), str(main)
    with mp.context() as context:
        # process is removed as first argument
        context.setattr(sys, 'argv', [process] + cmd)
        with pytest.raises(SystemExit) as result:
            main()
    code = utilo.returncode(result)
    assert (code == utilo.SUCCESS) == expect or expect is None, str(result)
    return code


@contextlib.contextmanager
def assert_run(command: str, cwd: str = None):
    done = utilo.run(command, cwd)
    assert done.returncode == utilo.SUCCESS, f'{done.stderr}\n{done.stdout}'
    yield done


@contextlib.contextmanager
def assert_run_fail(command: str, cwd: str = None):
    done = utilo.run(command, cwd, expect=False)
    assert done.returncode, f'{done.stderr}\n{done.stdout}'
    yield done


def single_execution() -> bool:
    """Check that test method is executed as single test.

    You can use this method to open the result in a web browser if test is
    executed with a human in front of the machine e.g. as a single test.

    >>> single_execution()
    False
    """
    frame = inspect.currentframe()
    caller = [item.function for item in inspect.getouterframes(frame)[0:9]]
    return any(item in sys.argv for item in caller)


def assert_success(process: subprocess.CompletedProcess):
    """Ensure that `process` completed correctly.

    If not a formatted information is logged
    """
    assert process, str(process)
    assert process.returncode == utilo.SUCCESS, utilo.format_completed(process)


def assert_failure(process: subprocess.CompletedProcess):
    """Ensure that `process` fails.

    If process completed correctly, a formatted information is logged.
    """
    assert process, str(process)
    assert process.returncode != utilo.SUCCESS, utilo.format_completed(process)


def create_cli_runner(package) -> '[typing.Callable, typing.Callable]':
    importlib.import_module(f'{package.__name__}.cli')
    main: callable = package.cli.main
    process: str = package.PROCESS
    # success
    success = functools.partial(
        run_cov,
        main=main,
        process=process,
        expect=True,
    )
    # failure
    failure = functools.partial(
        run_cov,
        main=main,
        process=process,
        expect=False,
    )
    return success, failure
