# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila


def clean_install(root, package):
    uninstall = 'pip uninstall %s -y' % package
    install = 'python setup.py install'

    clean_and_run = uninstall + ' && ' + install
    completed = utila.run(clean_and_run, cwd=root)
    assert completed.returncode == utila.SUCCESS, completed.stdout + completed.stderr


def install_and_run(root, package, executable=None):
    """Install and run --help to ensure basic function"""
    executable = executable if executable else package
    uninstall = 'pip uninstall %s -y' % package
    install = 'python setup.py install && %s --help' % executable

    clean_and_run = uninstall + ' && ' + install
    completed = utila.run(clean_and_run, cwd=root)
    assert completed.returncode == utila.SUCCESS, completed.stdout + completed.stderr
