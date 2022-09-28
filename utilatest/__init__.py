#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os

# baseline
from utilatest.baseline import BaseLineMixin
from utilatest.baseline import BaseLiner
# api calls
from utilatest.call import API_PREFIX
from utilatest.call import apicall
from utilatest.call import apidelete
from utilatest.call import apipost
from utilatest.call import apiput
from utilatest.call import apiupload
from utilatest.call import decode
from utilatest.call import delete
from utilatest.call import get
from utilatest.call import post
from utilatest.call import setup
from utilatest.call import upload
# file
from utilatest.file import increased_filecount
from utilatest.file import simplify_testfile_names
# install
from utilatest.install import clean_install
from utilatest.install import install_and_run
# log
from utilatest.log import log_raw
from utilatest.log import print_return
from utilatest.log import stderr
from utilatest.log import stdout
from utilatest.log import write_capsys
# run
from utilatest.runner import assert_failure
from utilatest.runner import assert_run
from utilatest.runner import assert_run_fail
from utilatest.runner import assert_success
from utilatest.runner import create_cli_runner
from utilatest.runner import run
from utilatest.runner import run_cov
from utilatest.runner import single_execution
# select
from utilatest.select import FASTRUN
from utilatest.select import LONGRUN
from utilatest.select import NIGHTLY
from utilatest.select import NONVIRTUAL
from utilatest.select import VIRTUAL
from utilatest.select import displayed
from utilatest.select import fixture_requires
from utilatest.select import hasbaw
from utilatest.select import hasgit
from utilatest.select import holyvalue
from utilatest.select import linux
from utilatest.select import longrun
from utilatest.select import nightly
from utilatest.select import no_linux
from utilatest.select import no_win
from utilatest.select import nonvirtual
from utilatest.select import register_marker
from utilatest.select import requires
from utilatest.select import step
from utilatest.select import virtual
from utilatest.select import win
# shortcuts
from utilatest.shortcuts import mp
from utilatest.shortcuts import td
# utils
from utilatest.utils import assert_bin
from utilatest.utils import binhash
from utilatest.utils import is_ci
from utilatest.utils import open_webbrowser
from utilatest.utils import simple
from utilatest.utils import test_resources
from utilatest.utils import testid
from utilatest.utils import worker_count

__version__ = '0.19.0'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PACKAGE = 'utilatest'

skip_longrun = longrun
skip_nightly = nightly
skip_nonvirtual = nonvirtual
skip_virtual = virtual
run_command = run_cov
# TODO: REMOVE log_raw with next increment
