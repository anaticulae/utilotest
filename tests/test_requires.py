# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# import os

import power
# import resinf
import utilo

TESTCODE = """\
import power
import resinf

import utilotest

resinf.setup(root='%s', validate=False)

@utilotest.requires(power.DOCU007_PDF)
def test_master():
    pass
"""

# def test_requires_singletd(td):
#     root = utilo.forward_slash(str(td.tmpdir))
#     testcode = TESTCODE % root
#     utilo.file_create(os.path.join(root, 'test_master.py'), testcode)
#     completed = utilo.run(f'pytest {root}')
#     assert '==== 1 skipped' in completed.stdout

# def test_requires_noskip(td):
#     root = utilo.forward_slash(str(td.tmpdir.join(utilo.tmpname())))
#     td.mkdir(root)
#     testcode = TESTCODE % root
#     os.makedirs(resinf.link(power.DOCU007_PDF, project=root))
#     utilo.file_create(os.path.join(root, 'test_master.py'), testcode)
#     completed = utilo.run(f'pytest {root}')
#     assert '1 skipped in' not in completed.stdout

STACK = """\
@utilotest.requires(power.DOCU007_PDF)
@utilotest.requires(power.DOCU009_PDF)
def test_stacked():
    pass
"""

# def test_requires_stacked_resource(td):
#     """Require more than one generated path to run test."""
#     root = utilo.forward_slash(str(td.tmpdir.join(utilo.tmpname())))
#     td.mkdir(root)
#     testcode = TESTCODE % root + STACK
#     utilo.file_create(os.path.join(root, 'test_master.py'), testcode)
#     os.makedirs(resinf.link(power.DOCU007_PDF, project=root))
#     completed = utilo.run(f'pytest {root}')
#     assert '1 passed, 1 skipped' in completed.stdout
