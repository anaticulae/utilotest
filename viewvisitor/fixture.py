# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import sys

import configos
import pytest
import selenium.webdriver
import utilo

import viewvisitor

linux = not sys.platform.startswith("win")


@pytest.fixture(scope='session')
def selenium_driver():
    if linux:
        pytest.skip('install selenium on linux.')
    if viewvisitor.FIREFOX_BINARY is None:
        utilo.error('DEFINE `FIREFOX_BINARY`')
        sys.exit(utilo.FAILURE)
    add_firefox_path()
    driver = selenium.webdriver.Firefox(
        firefox_binary=viewvisitor.FIREFOX_BINARY,
        executable_path=viewvisitor.FIREFOX_DRIVER,
    )
    yield driver
    # Teardown
    driver.quit()


def add_firefox_path():
    for item in (viewvisitor.FIREFOX_BINARY, viewvisitor.FIREFOX_DRIVER):
        utilo.exists_assert(item)
        base = utilo.path_parent(item)
        configos.env_path_append(base)
