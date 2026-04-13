#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import importlib.metadata
import os

# baseline
from utilotest.baseline import BaseLineMixin
from utilotest.baseline import BaseLiner
# api calls
from utilotest.call import API_PREFIX
from utilotest.call import apicall
from utilotest.call import apidelete
from utilotest.call import apipost
from utilotest.call import apiput
from utilotest.call import apiupload
from utilotest.call import decode
from utilotest.call import delete
from utilotest.call import get
from utilotest.call import post
from utilotest.call import setup
from utilotest.call import upload
# file
from utilotest.file import increased_filecount
from utilotest.file import simplify_testfile_names
# install
from utilotest.install import clean_install
from utilotest.install import install_and_run
from utilotest.install import install_package
# log
from utilotest.log import log_raw
from utilotest.log import print_return
from utilotest.log import stderr
from utilotest.log import stdout
from utilotest.log import write_capsys
# run
from utilotest.runner import assert_failure
from utilotest.runner import assert_run
from utilotest.runner import assert_run_fail
from utilotest.runner import assert_success
from utilotest.runner import create_cli_runner
from utilotest.runner import run
from utilotest.runner import run_cov
from utilotest.runner import single_execution
# select
from utilotest.select import FASTRUN
from utilotest.select import LONGRUN
from utilotest.select import NIGHTLY
from utilotest.select import NONVIRTUAL
from utilotest.select import VIRTUAL
from utilotest.select import displayed
from utilotest.select import fixture_requires
from utilotest.select import hasbaw
from utilotest.select import hasgit
from utilotest.select import hasprog
from utilotest.select import holyvalue
from utilotest.select import linux
from utilotest.select import longrun
from utilotest.select import monday
from utilotest.select import nightly
from utilotest.select import no_cov
from utilotest.select import no_linux
from utilotest.select import no_win
from utilotest.select import nonvirtual
from utilotest.select import register_marker
from utilotest.select import requires
from utilotest.select import step
from utilotest.select import virtual
from utilotest.select import win
# shortcuts
from utilotest.shortcuts import mp
from utilotest.shortcuts import td
# utils
from utilotest.utils import assert_bin
from utilotest.utils import binhash
from utilotest.utils import is_ci
from utilotest.utils import open_webbrowser
from utilotest.utils import simple
from utilotest.utils import test_resources
from utilotest.utils import testid
from utilotest.utils import worker_count

__version__ = importlib.metadata.version('utilotest')

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PACKAGE = 'utilotest'

skip_longrun = longrun
skip_nightly = nightly
skip_nonvirtual = nonvirtual
skip_virtual = virtual
run_command = run_cov
# TODO: REMOVE log_raw with next increment
