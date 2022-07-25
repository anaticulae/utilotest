# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import sys

import configo
import pytest
import selenium.webdriver
import utila

import viewvisitor


@pytest.fixture(scope='session')
def selenium_driver():
    if viewvisitor.FIREFOX_BINARY is None:
        utila.error('DEFINE `FIREFOX_BINARY`')
        sys.exit(utila.FAILURE)
    add_firefox_path()
    driver = selenium.webdriver.Firefox(
        firefox_binary=viewvisitor.FIREFOX_BINARY,
        executable_path=viewvisitor.FIREFOX_DRIVER,
    )
    yield driver
    # Teardown
    driver.quit()


def add_firefox_path():
    utila.exists_assert(viewvisitor.FIREFOX_BINARY)
    base = utila.path_parent(viewvisitor.FIREFOX_BINARY)
    configo.env_path_append(base)
