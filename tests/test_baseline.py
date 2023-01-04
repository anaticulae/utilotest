# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

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


def test_baseline_mixin_valid(td):
    td.mkdir('archive')
    utila.run('power -h >> archive/message')
    Simple().evaluate()


def test_baseline_mixin_invalid(td):
    td.mkdir('archive')
    utila.run('echo "invalid comparison" >> archive/message')
    with pytest.raises(AssertionError):
        Simple().evaluate()
