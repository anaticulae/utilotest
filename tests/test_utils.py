# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import webbrowser

import utila

import utilatest


def test_open_webbrowser(testdir, monkeypatch):
    # NOTE: don't know if that is a good test
    root = str(testdir)
    path = os.path.join(root, 'index.html')
    utila.file_create(path, 'Hello World')

    called = False

    def open_url(url, new=0, autoraise=True):  # pylint:disable=W0613
        nonlocal called
        called = True

    with monkeypatch.context() as context:
        context.setattr(utilatest, 'single_execution', lambda: True)
        context.setattr(webbrowser, 'open', open_url)
        with utilatest.open_webbrowser(path):
            pass
    assert called
