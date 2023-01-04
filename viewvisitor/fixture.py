# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import sys

import configo
import pytest
import selenium.webdriver
import utila

import viewvisitor

linux = not sys.platform.startswith("win")


@pytest.fixture(scope='session')
def selenium_driver():
    if linux:
        pytest.skip('install selenium on linux.')
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
    for item in [viewvisitor.FIREFOX_BINARY, viewvisitor.FIREFOX_DRIVER]:
        utila.exists_assert(item)
        base = utila.path_parent(item)
        configo.env_path_append(base)
