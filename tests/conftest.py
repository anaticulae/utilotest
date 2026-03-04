# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# import resinf

import utilotest
# TODO: AUTOMATE THIS
from utilotest import mp  # pylint:disable=W0611
from utilotest import td  # pylint:disable=W0611
from viewvisitor.fixture import selenium_driver  # pylint:disable=W0611

pytest_plugins = ['pytester', 'xdist', 'localserver']  # pylint: disable=invalid-name

# resinf.setup(utilotest.ROOT)
