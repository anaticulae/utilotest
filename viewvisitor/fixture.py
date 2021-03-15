# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import configo
import pytest
import selenium.webdriver
import utila

import viewvisitor


@pytest.fixture(scope='session')
def selenium_driver():
    if viewvisitor.FIREFOX_BINARY is None:
        utila.error('DEFINE `FIREFOX_BINARY`')
        exit(utila.FAILURE)
    base = os.path.split(viewvisitor.FIREFOX_BINARY)[0]
    # TODO: ADD ENV_PATH_APPEND METHOD
    path = f'{configo.env("PATH")};{base}'
    configo.env_set('PATH', path)
    driver = selenium.webdriver.Firefox(
        firefox_binary=viewvisitor.FIREFOX_BINARY,
        executable_path=viewvisitor.FIREFOX_DRIVER,
    )
    yield driver
    # Teardown
    driver.quit()
