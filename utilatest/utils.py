# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import os
import webbrowser

import utilatest


@contextlib.contextmanager
def open_webbrowser(path: str):
    """Open webbrowser on `give` path if test is used as single
    execution.

    Args:
        path(str): path to located html file
    Yields:
        None: to run operation to create website
    """
    yield
    assert os.path.exists(path), str(str)
    if utilatest.single_execution():
        webbrowser.open(path)
