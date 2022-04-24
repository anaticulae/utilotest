# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import power
import utila

TESTCODE = """\
import power

import utilatest

power.setup(root='%s')

@utilatest.requires(power.DOCU007_PDF)
def test_master():
    pass
"""


def test_requires_single(testdir):
    root = utila.forward_slash(str(testdir.tmpdir))
    testcode = TESTCODE % root
    utila.file_create(os.path.join(root, 'test_master.py'), testcode)
    completed = utila.run(f'pytest {root}')
    assert '==== 1 skipped' in completed.stdout


def test_requires_noskip(testdir):
    root = utila.forward_slash(str(testdir.tmpdir.join(utila.tmpname())))
    testdir.mkdir(root)
    testcode = TESTCODE % root
    os.makedirs(power.link(power.DOCU007_PDF, project=root))
    utila.file_create(os.path.join(root, 'test_master.py'), testcode)
    completed = utila.run(f'pytest {root}')
    assert '1 skipped in' not in completed.stdout


STACK = """\
@utilatest.requires(power.DOCU007_PDF)
@utilatest.requires(power.DOCU009_PDF)
def test_stacked():
    pass
"""


def test_requires_stacked_resource(testdir):
    """Require more than one generated path to run test."""
    root = utila.forward_slash(str(testdir.tmpdir.join(utila.tmpname())))
    testdir.mkdir(root)
    testcode = TESTCODE % root + STACK
    utila.file_create(os.path.join(root, 'test_master.py'), testcode)
    os.makedirs(power.link(power.DOCU007_PDF, project=root))
    completed = utila.run(f'pytest {root}')
    assert '1 passed, 1 skipped' in completed.stdout
