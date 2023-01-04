# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilatest


@utilatest.win
@utilatest.longrun
@utilatest.displayed
def test_selenium_driver(selenium_driver, httpserver):
    httpserver.serve_content('<div id="helmut">Helmut is talking</div>')
    # visit faked page
    selenium_driver.get(httpserver.url)
    text = selenium_driver.find_element_by_id('helmut').text
    assert text == 'Helmut is talking'
