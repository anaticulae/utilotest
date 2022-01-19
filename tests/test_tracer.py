# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest
import utila

import utilatest.cli.tracer


def test_tracer(testdir):
    # add file with traceback message
    utila.file_create('generated.log', utilatest.cli.tracer.TRACEBACK)
    # run tracer
    with pytest.raises(SystemExit):
        utilatest.cli.tracer.main()
    # collect result
    traced = utila.file_list(utilatest.cli.tracer.OUTPUTDIR)
    assert len(traced) == 1
