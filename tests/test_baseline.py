# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import sys

import pytest
import utila

import utilatest


class Simple(utilatest.BaseLiner):

    def __init__(self):
        super().__init__(
            program='power',
            step='help >> message',
            pages='',
            workdir='',
            source='',
            index='message',
            loader=lambda x: utila.file_read('message').strip(),
            archive='archive',
        )


@pytest.mark.skipif(
    not sys.platform.startswith("win"),
    reason='pdfcat does not work on linux',
)
def test_baseline_mixin_valid(td):
    td.mkdir('archive')
    utila.run('power -h >> archive/message')
    Simple().evaluate()


def test_baseline_mixin_invalid(td):
    td.mkdir('archive')
    utila.run('echo "invalid comparison" >> archive/message')
    with pytest.raises(AssertionError):
        Simple().evaluate()
