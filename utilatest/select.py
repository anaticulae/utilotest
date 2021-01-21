#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os

import pytest

VIRTUAL_ENVKEY = 'VIRTUAL'
VIRTUAL = VIRTUAL_ENVKEY in os.environ
NONVIRTUAL = not VIRTUAL

FAST = 'FAST' in os.environ.keys()
NIGHTLY = 'NIGHTLY' in os.environ.keys()
LONGRUN = 'LONGRUN' in os.environ.keys() or NIGHTLY
FASTRUN = not LONGRUN or FAST

LONGRUN_REASON = 'test requires to much time'
VIRTUAL_REASON = 'require virtual environment'
NONVIRTUAL_REASON = 'require non virtual environment'

# pylint: disable=invalid-name
skip_longrun = pytest.mark.skipif(FASTRUN, reason=LONGRUN_REASON)
skip_nightly = pytest.mark.skipif(FASTRUN or not NIGHTLY, reason=LONGRUN_REASON)
skip_nonvirtual = pytest.mark.skipif(NONVIRTUAL, reason=VIRTUAL_REASON)
skip_virtual = pytest.mark.skipif(VIRTUAL, reason=NONVIRTUAL_REASON)

longrun = skip_longrun
nightly = skip_nightly
nonvirtual = skip_nonvirtual
virtual = skip_virtual

# mark tests to optimize holy value parameters
"""After upgrading pytest, markers must be registered in pytest config.
To avoid putting holyvalue markers in every pytest.ini we bypass them by
directly acessing the pytest API. This may fail in the future. old:
holyvalue = pytest.mark.holyvalue"""
holyvalue = pytest.mark._markers.add('holyvalue')  # pylint:disable=W0212
# TODO: SUPPORT holyvalue('rawmaker.features.text.MAX_WIDTH')
