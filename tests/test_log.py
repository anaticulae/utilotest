# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest
import utila

import utilatest


def test_log_raw(capsys):
    content = 'Hello\nHello\nHello'

    with pytest.raises(AssertionError):
        assert len(content) > 1000, utilatest.log_raw(content)

    assert content in utilatest.stdout(capsys)


def test_stdout_stderr(capsys):
    utila.error('abc')
    assert 'abc' in utilatest.stderr(capsys)

    utila.log('www')
    assert 'www' in utilatest.stdout(capsys)


EXPECTED = """\
Before
A
10
B
      100
After
"""


def test_printresult(capsys):

    @utilatest.print_return
    def buddy(value):
        utila.log('A')
        utila.log(value)
        utila.log('B')
        return value * value

    utila.log('Before')
    with utila.level_tmp(utila.Level.DEBUG):
        buddy(10)
    utila.log('After')
    current = utilatest.stdout(capsys)
    assert current == EXPECTED
