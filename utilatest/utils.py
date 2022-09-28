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


def test_resources(resources):
    """Remove `pages` from resource definition.

    >>> import power;import utilatest;power.setup(utilatest.ROOT);
    >>> test_resources([power.BACHELOR090_PDF, (power.MASTER116_PDF, ':')])
    [ParameterSet(values=(...bachelor090.pdf',), marks=(...missing:...master116.pdf',),...id='master116')]
    """
    import power
    unique = [item if isinstance(item, str) else item[0] for item in resources]
    assert len(unique) == len(set(unique)), 'duplicated resources'
    result = []
    for item in unique:
        generated = power.link(item)
        skip = not utila.exists(generated)
        testname = utila.file_name(item)
        result.append(
            pytest.param(
                item,
                id=testname,
                marks=pytest.mark.skipif(skip, reason=f'missing: {generated}'),
            ))
    return result


def worker_count(number: int, onci: int) -> int:
    """Determine worker depending running on ci or not.

    >>> str(worker_count(5, onci=10))
    '...'
    """
    if is_ci():
        return onci
    return number


def is_ci() -> bool:
    """\
    >>> str(is_ci())
    '...'
    """
    if os.environ.get('JENKINS_HOME', False):
        return True
    return False
