# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import utilatest
import utilatest.utils


def test_test_log_raw(capsys):
    content = 'Hello\nHello\nHello'

    with pytest.raises(AssertionError):
        assert len(content) > 1000, utilatest.log_raw(content)

    assert content in capsys.readouterr().out
