# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest
import utila

import utilatest


def test_run(tmpdir):
    completed = utilatest.run('dir', tmpdir)
    assert completed.returncode == utila.SUCCESS

    with utilatest.assert_run('dir', tmpdir) as result:
        assert result.returncode == utila.SUCCESS

    with utilatest.assert_run_fail('this is not a command', tmpdir) as result:
        assert result.returncode == utila.FAILURE


def test_test_run_command(monkeypatch):

    def main():
        # example runnable
        exit(utila.SUCCESS)

    utilatest.run_command('--number 10', 'main', main, True, monkeypatch)


def test_test_assert_success():
    completed = utilatest.run('python --help')
    utilatest.assert_success(completed)


def test_test_assert_success_failed():
    completed = utilatest.run('python --helpsambadamba', expect=None)
    with pytest.raises(AssertionError):
        utilatest.assert_success(completed)


def test_test_assert_failure():
    completed = utilatest.run('python --helpsambadamba', expect=None)
    utilatest.assert_failure(completed)


def test_test_assert_failure_failed():
    completed = utilatest.run('python --help')
    with pytest.raises(AssertionError):
        utilatest.assert_failure(completed)
