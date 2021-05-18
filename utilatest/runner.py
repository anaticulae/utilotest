# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import inspect
import os
import subprocess  # nosec
import sys

import pytest
import utila

import utilatest


def run(
        cmd: str,
        cwd: str = None,
        env: dict = None,
        expect: bool = True,
        verbose: bool = False,
) -> subprocess.CompletedProcess:
    """Run external process

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
        utila.log(f'cd {cwd}')
        utila.log(cmd)

    completed = subprocess.run(  # nosec
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
        utilatest.assert_success(completed)
    if expect is False:
        utilatest.assert_failure(completed)
    return completed


def run_command(
        cmd: str,
        process: str,
        main: callable,
        success: bool,
        monkeypatch,
) -> int:
    """Run `main` with `command`

    Args:
        cmd(str): command to run
        process(str): name of executed tool
        main(callable): method to run
        success(bool): expectation that process succeeds or fails
        monkeypatch(fixture): pytest patch feature
    Returns:
        Return code of completed process.
    """
    with contextlib.suppress(AttributeError):
        cmd = cmd.split()
    assert callable(main), str(main)

    with monkeypatch.context() as context:
        # process is removed as first argument
        context.setattr(sys, 'argv', [process] + cmd)
        with pytest.raises(SystemExit) as result:
            main()
    code = utila.returncode(result)
    assert (code == utila.SUCCESS) == success, str(result)
    return code


@contextlib.contextmanager
def assert_run(command: str, cwd: str = None):
    done = utila.run(command, cwd)
    assert done.returncode == utila.SUCCESS, f'{done.stderr}\n{done.stdout}'
    yield done


@contextlib.contextmanager
def assert_run_fail(command: str, cwd: str = None):
    done = utila.run(command, cwd, expect=False)
    assert done.returncode, f'{done.stderr}\n{done.stdout}'
    yield done


def single_execution() -> bool:
    """Check that test method is executed as single test. You can use
    this method to open the result in a web browser if test is executed
    with a human in front of the machine eg. as a single test.

    >>> single_execution()
    False
    """
    frame = inspect.currentframe()
    caller = [item.function for item in inspect.getouterframes(frame)[0:5]]
    return any([item in sys.argv for item in caller])


def assert_success(process: subprocess.CompletedProcess):
    """Ensure that `process` completed correctly, if not a formated
    information is logged"""
    assert process, str(process)
    assert process.returncode == utila.SUCCESS, utila.format_completed(process)


def assert_failure(process: subprocess.CompletedProcess):
    """Ensure that `process` fails. If process completed correctly, a
    formated information is logged."""
    assert process, str(process)
    assert process.returncode != utila.SUCCESS, utila.format_completed(process)
