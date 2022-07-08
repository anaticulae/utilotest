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


def test_test_increased_filecount(td):
    with utilatest.increased_filecount(td.tmpdir):
        utila.file_create('test.txt')


def test_test_increased_filecount_with_number(td):
    with utilatest.increased_filecount(td.tmpdir, mindiff=1, maxdiff=1):
        utila.file_create('test.txt')


def test_test_increased_filecount_with_ext(td):
    with pytest.raises(AssertionError):
        with utilatest.increased_filecount(td.tmpdir, ext='*.pdf'):
            utila.file_create('test_abc.txt')


def test_test_increased_filecount_to_few_created(td):
    with pytest.raises(AssertionError):
        with utilatest.increased_filecount(td.tmpdir):
            pass
    with pytest.raises(AssertionError):
        with utilatest.increased_filecount(td.tmpdir, mindiff=2):
            utila.file_create('test.txt')
