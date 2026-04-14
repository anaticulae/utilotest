# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import webbrowser

# pylint: disable=wrong-import-order
import power
import utilo

import utilotest


def test_open_webbrowser(td, mp):
    # NOTE: don't know if that is a good test
    path = utilo.join(td.tmpdir, 'index.html')
    utilo.file_create(path, 'Hello World')

    called = False

    def open_url(url, new=0, autoraise=True):  # pylint:disable=W0613
        nonlocal called
        called = True

    with mp.context() as context:
        context.setattr(utilotest, 'single_execution', lambda: True)
        context.setattr(webbrowser, 'open', open_url)
        with utilotest.open_webbrowser(path):
            pass
    assert called


def test_test_resources():

    def markme(item):
        if item == power.BACHELOR028_PDF:
            return utilotest.longrun
        return None

    resources = utilotest.test_resources(
        [
            power.BACHELOR028_PDF,
            power.MASTER116_PDF,
        ],
        marker=markme,
    )
    raw = str(resources)
    assert 'longrun' in raw
