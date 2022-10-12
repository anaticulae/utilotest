#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os
import sys

import pytest
import utila

VIRTUAL_ENVKEY = 'VIRTUAL'
VIRTUAL = VIRTUAL_ENVKEY in os.environ
NONVIRTUAL = not VIRTUAL

FAST = 'FAST' in os.environ
NIGHTLY = 'NIGHTLY' in os.environ
LONGRUN = 'LONGRUN' in os.environ or NIGHTLY
MONDAY = 'MONDAY' in os.environ
FASTRUN = FAST and not NIGHTLY and not MONDAY

LONGRUN_REASON = 'requires too much time'
VIRTUAL_REASON = 'require venv'
NONVIRTUAL_REASON = 'require non-venv'
MONDAY_REASON = 'its not monday'

WIN = 'win' in sys.platform
LIN = not WIN

# pylint: disable=invalid-name
longrun = pytest.mark.skipif(FASTRUN, reason=LONGRUN_REASON)
nightly = pytest.mark.skipif(FASTRUN or not NIGHTLY, reason=LONGRUN_REASON)
monday = pytest.mark.skipif(not MONDAY, reason=MONDAY_REASON)
nonvirtual = pytest.mark.skipif(NONVIRTUAL, reason=VIRTUAL_REASON)
virtual = pytest.mark.skipif(VIRTUAL, reason=NONVIRTUAL_REASON)
hasgit = pytest.mark.skipif(
    utila.run('git help', expect=None).returncode,
    reason='require git',
)
hasbaw = pytest.mark.skipif(
    utila.run('baw --help', expect=None).returncode,
    reason='require baw',
)

linux = pytest.mark.skipif(not LIN, reason='linux only')
win = pytest.mark.skipif(not WIN, reason='windows only')
no_win = pytest.mark.skipif(WIN, reason='no windows')
no_linux = pytest.mark.skipif(LIN, reason='no linux')


def register_marker(name: str):
    """After upgrading pytest, markers must be registered in pytest
    config. To avoid putting holyvalue markers in every pytest.ini we
    bypass them by directly acessing the pytest API. This may fail in
    the future."""
    pytest.mark._markers.add(name)  # pylint:disable=W0212
    return getattr(pytest.mark, name)


longrun = register_marker('longrun')
nightly = register_marker('nightly')

# mark tests to optimize holy value parameters
# old: holyvalue = pytest.mark.holyvalue
holyvalue = register_marker('holyvalue')
displayed = register_marker('displayed')
# TODO: SUPPORT holyvalue('rawmaker.features.text.MAX_WIDTH')


def requires(resource, folder=None):
    exists = _exists(resource, folder)
    if utila.iterable(resource):  # pylint:disable=W0160
        resource = [utila.forward_slash(item) for item in resource]
    else:
        resource = utila.forward_slash(resource)
    marker = pytest.mark.skipif(
        not exists,
        reason=f'require/generated: {resource}; folder: {folder}',
    )
    return marker


def fixture_requires(resource, folder=None):
    if _exists(resource, folder):
        return
    if utila.iterable(resource):  # pylint:disable=W0160
        resource = [utila.forward_slash(item) for item in resource]
    else:
        resource = utila.forward_slash(resource)
    pytest.skip(f'require/generated: {resource}; folder: {folder}')


def _exists(resource, folder=None):
    if utila.iterable(resource):
        return all(_exists(item, folder=folder) for item in resource)
    import power  # pylint:disable=import-outside-toplevel
    exists = os.path.exists(power.link(resource, folder=folder))
    # non generated resources
    exists |= os.path.exists(resource) and resource not in power.RESOURCES
    return exists


def step(source, pages: tuple = None, reason=None, marks=None, ids=None):
    if ids is None:
        ids = utila.file_name(source)
    if reason:
        if marks:
            # fail = pytest.mark.xfail(reason=reason)
            assert 0, 'not implemented yet'
        else:
            marks = pytest.mark.xfail(reason=reason)
    if marks:  # pylint:disable=W0160
        result = pytest.param(source, pages, marks=marks, id=ids)
    else:
        result = pytest.param(source, pages, id=ids)
    return result
