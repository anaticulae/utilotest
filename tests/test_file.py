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


def test_increased_filecount(td):
    with utilotest.increased_filecount(td.tmpdir):
        utilo.file_create('test.txt')


def test_increased_filecount_with_number(td):
    with utilotest.increased_filecount(td.tmpdir, mindiff=1, maxdiff=1):
        utilo.file_create('test.txt')


def test_increased_filecount_with_ext(td):
    with pytest.raises(AssertionError):
        with utilotest.increased_filecount(td.tmpdir, ext='*.pdf'):
            utilo.file_create('test_abc.txt')


def test_increased_filecount_to_few_created(td):
    with pytest.raises(AssertionError):
        with utilotest.increased_filecount(td.tmpdir):
            pass
    with pytest.raises(AssertionError):
        with utilotest.increased_filecount(td.tmpdir, mindiff=2):
            utilo.file_create('test.txt')
