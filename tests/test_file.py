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


def test_test_increased_filecount(testdir):
    root = str(testdir)
    with utilatest.increased_filecount(root):
        utila.file_create('test.txt')


def test_test_increased_filecount_with_number(testdir):
    root = str(testdir)
    with utilatest.increased_filecount(root, mindiff=1, maxdiff=1):
        utila.file_create('test.txt')


def test_test_increased_filecount_with_ext(testdir):
    root = str(testdir)
    with pytest.raises(AssertionError):
        with utilatest.increased_filecount(root, ext='*.pdf'):
            utila.file_create('test_abc.txt')


def test_test_increased_filecount_to_few_created(testdir):
    root = str(testdir)
    with pytest.raises(AssertionError):
        with utilatest.increased_filecount(root):
            pass

    with pytest.raises(AssertionError):
        with utilatest.increased_filecount(root, mindiff=2):
            utila.file_create('test.txt')
