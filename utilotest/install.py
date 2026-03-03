# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

import utilotest

UNINSTALL = 'pip uninstall %s -y'
INSTALL = 'python setup.py install'


def install_package(root):
    utilo.exists_assert(root)
    completed = utilo.run(INSTALL, cwd=root)
    error = utilotest.stdout(completed) + utilotest.stderr(completed)
    assert completed.returncode == utilo.SUCCESS, error


def clean(package):
    completed = utilo.run(UNINSTALL % package)
    error = utilotest.stdout(completed) + utilotest.stderr(completed)
    assert completed.returncode == utilo.SUCCESS, error


def clean_install(root, package):
    clean(package)
    install_package(root)


def install_and_run(
    root,
    package,
    executable=None,
    cleanx: bool = True,
):
    """Install and run --help to ensure basic function"""
    executable = executable if executable else package
    install = f'python setup.py install && {executable} --help'
    if cleanx:
        clean(package)
    completed = utilo.run(install, cwd=root)
    error = utilotest.stdout(completed) + utilotest.stderr(completed)
    assert completed.returncode == utilo.SUCCESS, error
