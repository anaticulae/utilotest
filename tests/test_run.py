# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import sys

import pytest
import utilo

import utilotest


def test_run(tmpdir):
    completed = utilotest.run('ls', tmpdir)
    assert completed.returncode == utilo.SUCCESS

    with utilotest.assert_run('ls', tmpdir) as result:
        assert result.returncode == utilo.SUCCESS  # pylint:disable=E1101

    with utilotest.assert_run_fail('this is not a command', tmpdir) as result:
        assert result.returncode >= utilo.FAILURE  # pylint:disable=E1101


def test_run_cov(mp):

    def main():
        # example runnable
        sys.exit(utilo.SUCCESS)

    utilotest.run_cov(
        '--number 10',
        'main',
        main,
        expect=True,
        mp=mp,
    )


def test_assert_success():
    completed = utilotest.run('python --help')
    utilotest.assert_success(completed)


def test_assert_success_failed():
    completed = utilotest.run('python --helpsambadamba', expect=None)
    with pytest.raises(AssertionError):
        utilotest.assert_success(completed)


def test_assert_failure():
    completed = utilotest.run('python --helpsambadamba', expect=None)
    utilotest.assert_failure(completed)


def test_assert_failure_failed():
    completed = utilotest.run('python --help')
    with pytest.raises(AssertionError):
        utilotest.assert_failure(completed)
