# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import binascii
import contextlib
import os
import re
import webbrowser

import pytest
import utila

import utilatest


@contextlib.contextmanager
def open_webbrowser(path: str):
    """Open webbrowser on `give` path if test is used as single
    execution.

    Args:
        path(str): path to located html file
    Yields:
        None: to run operation to create website
    """
    yield
    assert os.path.exists(path), str(str)
    if utilatest.single_execution():
        webbrowser.open(path)


SIMPLIFY = str.maketrans({item: '' for item in ' _-=+,.;\'/"()!@#$%^&&*'})


def simple(item: str, maxlength: int = 25) -> str:
    """Simplify test name to ease selecting generated tests by test name.

    >>> simple('No spaces _+; 133')
    'Nospaces133'
    """
    item = utila.fix_encoding(item)
    item = item.translate(SIMPLIFY)
    item = item[-maxlength:]
    return item


def binhash(data: bytes) -> int:
    """\
    >>> binhash(b'hello')
    907060870
    """
    result = binascii.crc32(data)
    return result


def assert_bin(data: bytes, expected: int):
    current = binhash(data)
    assert current == expected, f'{current}=={expected}'


def testid() -> str:
    """\
    >>> testid()
    'utilatest.utils.testid'
    """
    # TODO: DIRTY
    test = os.environ['PYTEST_CURRENT_TEST']
    try:
        result = re.search(r'\[(.+)\]', test)[1]
    except TypeError:
        result = re.search(r'\:\:(.+)[ ]', test)[1]
    return result


def test_resources(files):
    """Remove `pages` from resource definition."""
    result = []
    for item in files:
        if isinstance(item, tuple):
            item = item[0]
        result.append(pytest.param(item, id=utila.file_name(item)))
    return result
