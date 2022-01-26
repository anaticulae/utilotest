# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import subprocess  # nosec
import warnings

import utila


def write_capsys(capsys, path: str = None):
    """Save logged capsys to filespace."""
    stdout_, stderr_ = stdout(capsys), stderr(capsys)
    change = utila.chdir if path else utila.nothing
    with change(path):
        utila.file_create('logging.txt', stdout_)
        utila.file_create('error.txt', stderr_)


def log_raw(content: str):
    """Print `content` which raises an AssertError. Fix encoding if
    non-utf8 character are printed.

    Hint: Avoid using print() to reduse finding 'print' when searching
    in code base.

    Example:
        asssert len(abc) > 100, utila.log_raw(abc)
    """
    warnings.warn('use utila.log_raw, will removed with utilatest 1.0.0')
    content = utila.string.fix_encoding(content)
    print(content, flush=True)


def stderr(capsys) -> str:
    if isinstance(capsys, subprocess.CompletedProcess):
        return capsys.stderr
    return capsys.readouterr().err


def stdout(capsys) -> str:
    if isinstance(capsys, subprocess.CompletedProcess):
        return capsys.stdout
    return capsys.readouterr().out


def print_return(user_function):

    def decorator(*args, **kwds):
        result = user_function(*args, **kwds)
        utila.debug(result)
        return result

    return decorator
