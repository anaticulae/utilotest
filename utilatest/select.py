#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os
import sys

import pytest
import resinf
import utila

VIRTUAL_ENVKEY = 'VIRTUAL'
VIRTUAL = VIRTUAL_ENVKEY in os.environ
NONVIRTUAL = not VIRTUAL

FAST = 'FAST' in os.environ
NIGHTLY = 'NIGHTLY' in os.environ
LONGRUN = 'LONGRUN' in os.environ or NIGHTLY
MONDAY = 'MONDAY' in os.environ
FASTRUN = FAST and not NIGHTLY and not MONDAY

VIRTUAL_REASON = 'require venv'
NONVIRTUAL_REASON = 'require non-venv'
MONDAY_REASON = 'its not monday'

WIN = 'win' in sys.platform
LIN = not WIN
COV = 'coverage' in sys.modules

# pylint: disable=invalid-name
monday = pytest.mark.skipif(not MONDAY, reason=MONDAY_REASON)
nonvirtual = pytest.mark.skipif(NONVIRTUAL, reason=VIRTUAL_REASON)
virtual = pytest.mark.skipif(VIRTUAL, reason=NONVIRTUAL_REASON)


def hasprog(prog, msg=''):
    if not msg:
        msg = f'install {prog}'
    has = pytest.mark.skipif(
        not utila.hasprog(prog),
        reason=msg,
    )
    return has


hasgit = hasprog('git')
hasbaw = hasprog('baw')

linux = pytest.mark.skipif(not LIN, reason='linux only')
win = pytest.mark.skipif(not WIN, reason='windows only')
no_win = pytest.mark.skipif(WIN, reason='no windows')
no_linux = pytest.mark.skipif(LIN, reason='no linux')
no_cov = pytest.mark.skipif(COV, reason='skip on cov run')


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
    exists = os.path.exists(resinf.link(resource, folder=folder))
    # non generated resources
    import power  # pylint:disable=import-outside-toplevel
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
