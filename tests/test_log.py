# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest
import utilo

import utilotest


def test_log_raw(capsys):
    content = 'Hello\nHello\nHello'

    with pytest.raises(AssertionError):
        assert len(content) > 1000, utilotest.log_raw(content)

    assert content in utilotest.stdout(capsys)


def test_stdout_stderr(capsys):
    utilo.error('abc')
    assert 'abc' in utilotest.stderr(capsys)

    utilo.log('www')
    assert 'www' in utilotest.stdout(capsys)


EXPECTED = """\
Before
A
10
B
      100
After
"""


def test_printresult(capsys):

    @utilotest.print_return
    def buddy(value):
        utilo.log('A')
        utilo.log(value)
        utilo.log('B')
        return value * value

    utilo.log('Before')
    with utilo.level_tmp(utilo.Level.DEBUG):
        buddy(10)
    utilo.log('After')
    current = utilotest.stdout(capsys)
    assert current == EXPECTED
