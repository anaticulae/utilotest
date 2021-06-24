# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila

TESTCODE = """\
import power

import utilatest

power.setup(root='%s')

@utilatest.requires(power.DOCU07_PDF)
def test_master():
    pass
"""


def test_requires_single(testdir):
    root = utila.forward_slash(str(testdir.tmpdir))
    testcode = TESTCODE % root
    utila.file_create(os.path.join(root, 'test_master.py'), testcode)
    completed = utila.run(f'pytest {root}')
    assert '1 skipped in' in completed.stdout


def test_requires_noskip(testdir):
    root = utila.forward_slash(str(testdir.tmpdir))
    testcode = TESTCODE % root
    utila.file_create(os.path.join(root, 'test_master.py'), testcode)
    os.makedirs(os.path.join(root, 'tests/resources/generated/docu_docu007'))
    completed = utila.run(f'pytest {root}')
    assert '1 skipped in' not in completed.stdout
