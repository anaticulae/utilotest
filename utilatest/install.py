# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import utilatest

UNINSTALL = 'pip uninstall %s -y'
INSTALL = 'python setup.py install'


def clean_install(root, package):
    clean_and_run = UNINSTALL % package + ' && ' + INSTALL
    completed = utila.run(clean_and_run, cwd=root)
    error = utilatest.stdout(completed) + utilatest.stderr(completed)
    assert completed.returncode == utila.SUCCESS, error


def install_and_run(root, package, executable=None):
    """Install and run --help to ensure basic function"""
    executable = executable if executable else package
    install = 'python setup.py install && %s --help' % executable
    clean_and_run = UNINSTALL % package + ' && ' + install
    completed = utila.run(clean_and_run, cwd=root)
    error = utilatest.stdout(completed) + utilatest.stderr(completed)
    assert completed.returncode == utila.SUCCESS, error
