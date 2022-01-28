# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import functools
import os
import sys

import utila

GIT_REPLACE = utila.parse_state(os.environ.get('DEV_GIT_REPLACE', None))


class BaseLineMixin:

    def __init__(self, cmd, workdir, index, archive):
        self.cmd = cmd
        self.workdir = workdir
        self.index = index
        self.archive = archive

    def evaluate(self):
        self.generate()
        loaded = self.load()
        rawvalue = self.raw(loaded)
        expected, path = self.expected
        if rawvalue != expected:
            outpath = os.path.join(self.workdir, 'baseline')
            utila.error('write baseline')
            utila.file_create(outpath, rawvalue)
            if GIT_REPLACE:
                # ease debugging due git --diff
                withnewline = rawvalue.rstrip() + utila.NEWLINE
                utila.file_replace(path, withnewline)
        if self.expected is None:
            with contextlib.suppress(AttributeError):
                self.backup(loaded)
                return
        elif rawvalue != expected:
            utila.log('EXPECTED:')
            utila.log(expected)
            utila.log('GIVEN:')
            utila.log(rawvalue)
        assert rawvalue == expected

    def generate(self):
        if isinstance(self.cmd, str):
            utila.run(cmd=self.cmd, cwd=self.workdir)
            return
        # run partial function
        self.cmd()

    def raw(self, value) -> str:  # pylint:disable=R0201
        return str(value)

    def load(self):  # pylint:disable=R0201
        return ''

    @functools.cached_property
    def expected(self) -> str:
        inpath = os.path.join(self.archive, str(self.index))
        if not os.path.exists(inpath):
            utila.error('empty archive data')
            return None, inpath
        loaded = utila.file_read(inpath)
        # rstrip to enable spaces as empty content of a expected tabel for
        # example.
        result = loaded.rstrip()
        return result, inpath


class BaseLiner(BaseLineMixin):

    def __init__(
        self,
        program,
        step,
        pages,
        workdir,
        source,
        archive,
        loader,
        index=None,
        convert_source: bool = True,
    ):
        super().__init__(
            cmd=self.tocmd(program, step, pages, source, workdir,
                           convert_source),
            workdir=workdir,
            index=index if index else utila.file_name(source),
            archive=archive,
        )
        self.loader = loader

    @staticmethod
    def tocmd(program, step, pages, source, workdir, convert_source=True):
        source = convert_ifpossible(source, convert=convert_source)
        assert not source or utila.exists(source), str(source)
        pages = f'--pages={pages}' if pages else ''
        source = f'-i={source}' if source else ''
        workdir = f'-o={workdir}' if workdir else ''
        step = f'--{step}' if step else ''
        todo = f'{step} {pages} {source} {workdir}'
        if isinstance(program, str):
            result = f'{program} {todo}'
        else:
            result = functools.partial(program, todo)
        return result

    def load(self) -> str:
        loaded = self.loader(self.workdir)
        return loaded


def convert_ifpossible(source, convert: bool = False):
    if not source:
        return ''
    if not convert:
        return source
    try:
        import power
    except ModuleNotFoundError:  # pragma: no cover
        utila.error('require power')
        sys.exit(utila.FAILURE)
    source = power.link(source)
    return source
