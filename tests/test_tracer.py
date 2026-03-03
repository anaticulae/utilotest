# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest
import utilo

import utilotest.cli.tracer

TRACEBACK = """
[ERROR] Traceback (most recent call last):
  File "C:/tmp/baw/venv/queuemo/lib/site-packages/utilo/feature/processor.py", line 238, in run_hook_safely
    result = utilo.pass_required(caller=hook.work, pages=pages, **argv)
  File "C:/tmp/baw/venv/queuemo/lib/site-packages/utilo/typechecker.py", line 309, in pass_required
    result = caller(**data)
  File "C:/tmp/baw/venv/queuemo/lib/site-packages/groupme/feature/footer.py", line 61, in work
    result = extract_footerheader(
"""

INVALID_CLI = """
usage: bibliography [-h] [-i INPUT] [-o OUTPUT] [-j JOB] [-V]
bibliography: error: unrecognized arguments: --bibs
"""


@pytest.mark.parametrize('error', (
    pytest.param(TRACEBACK, id='python error'),
    pytest.param(INVALID_CLI, id='invalid cli'),
))
def test_tracer(error, td):  # pylint:disable=W0613
    # add file with traceback message
    utilo.file_create('generated.log', error)
    # run tracer
    with pytest.raises(SystemExit):
        utilotest.cli.tracer.main()
    # collect result
    traced = utilo.file_list(utilotest.cli.tracer.OUTPUTDIR)
    assert len(traced) == 1
