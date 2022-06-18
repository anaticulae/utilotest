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

TRACEBACK = """
[ERROR] Traceback (most recent call last):
  File "C:/tmp/baw/venv/queuemo/lib/site-packages/utila/feature/processor.py", line 238, in run_hook_safely
    result = utila.pass_required(caller=hook.work, pages=pages, **argv)
  File "C:/tmp/baw/venv/queuemo/lib/site-packages/utila/typechecker.py", line 309, in pass_required
    result = caller(**data)
  File "C:/tmp/baw/venv/queuemo/lib/site-packages/groupme/feature/footer.py", line 61, in work
    result = extract_footerheader(
"""


@pytest.mark.parametrize('error', (pytest.param(TRACEBACK, id='python error'),))
def test_tracer(error, testdir):
    # add file with traceback message
    utila.file_create('generated.log', error)
    # run tracer
    with pytest.raises(SystemExit):
        utilatest.cli.tracer.main()
    # collect result
    traced = utila.file_list(utilatest.cli.tracer.OUTPUTDIR)
    assert len(traced) == 1
