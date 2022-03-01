# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import utilatest

PACKAGE = """\
import setuptools
setuptools.setup(
    name='%s',
    packages=['%s'],
)
"""


@utilatest.skip_nonvirtual
@utilatest.longrun
def test_clean_install(testdir):
    package = 'dorimifasa'
    testdir.mkdir(package)
    utila.file_create(
        testdir.tmpdir.join('setup.py'),
        PACKAGE % (package, package),
    )
    utila.run('python setup.py build')
    utilatest.clean_install(
        testdir.tmpdir,
        'dorimifasa',
    )


@utilatest.skip_nonvirtual
@utilatest.longrun
def test_install_and_run(testdir):
    package = 'dorimifasamore'
    testdir.mkdir(package)
    utila.file_create(
        testdir.tmpdir.join('setup.py'),
        PACKAGE % (package, package),
    )
    utila.run('python setup.py build')
    utilatest.install_and_run(
        root=testdir.tmpdir,
        package=package,
        executable='power',  # not the installed one
    )
