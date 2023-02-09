# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2022-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila

GIT_REPLACE = utila.parse_state(os.environ.get('BASELINE_REPLACE', None))
# TODO: REMOVE LATER
GIT_REPLACE |= utila.parse_state(os.environ.get('DEV_GIT_REPLACE', None))
