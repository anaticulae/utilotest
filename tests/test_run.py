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
import utila

import utilatest


def test_run(tmpdir):
    completed = utilatest.run('ls', tmpdir)
    assert completed.returncode == utila.SUCCESS

    with utilatest.assert_run('ls', tmpdir) as result:
        assert result.returncode == utila.SUCCESS  # pylint:disable=E1101

    with utilatest.assert_run_fail('this is not a command', tmpdir) as result:
        assert result.returncode >= utila.FAILURE  # pylint:disable=E1101


def test_run_cov(mp):

    def main():
        # example runnable
        sys.exit(utila.SUCCESS)

    utilatest.run_cov(
        '--number 10',
        'main',
        main,
        expect=True,
        mp=mp,
    )


def test_assert_success():
    completed = utilatest.run('python --help')
    utilatest.assert_success(completed)


def test_assert_success_failed():
    completed = utilatest.run('python --helpsambadamba', expect=None)
    with pytest.raises(AssertionError):
        utilatest.assert_success(completed)


def test_assert_failure():
    completed = utilatest.run('python --helpsambadamba', expect=None)
    utilatest.assert_failure(completed)


def test_assert_failure_failed():
    completed = utilatest.run('python --help')
    with pytest.raises(AssertionError):
        utilatest.assert_failure(completed)
