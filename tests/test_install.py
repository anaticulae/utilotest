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


@utilatest.nonvirtual
@utilatest.longrun
def test_clean_install(td):
    package = 'dorimifasa'
    td.mkdir(package)
    utila.file_create(
        td.tmpdir.join('setup.py'),
        PACKAGE % (package, package),
    )
    utila.run('python setup.py build')
    utilatest.clean_install(
        td.tmpdir,
        'dorimifasa',
    )


@utilatest.nonvirtual
@utilatest.longrun
def test_install_and_run(td):
    package = 'dorimifasamore'
    td.mkdir(package)
    utila.file_create(
        td.tmpdir.join('setup.py'),
        PACKAGE % (package, package),
    )
    utila.run('python setup.py build')
    utilatest.install_and_run(
        root=td.tmpdir,
        package=package,
        executable='power',  # not the installed one
    )
