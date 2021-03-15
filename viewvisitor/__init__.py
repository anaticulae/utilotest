# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utilatest
from viewvisitor.fixture import selenium_driver  # pylint:disable=W0611

ROOT = os.path.join(utilatest.ROOT, 'viewvisitor')

FIREFOX_DRIVER = os.path.join(ROOT, 'fuchs/geckodriver.exe')
FIREFOX_BINARY = os.getenv('FIREFOX_BINARY', default=None)
