# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import glob
import os

import utila
import utila.file
import utila.logger
import utila.string


def simplify_testfile_names(files, ext='pdf', sort: bool = True) -> tuple:
    """Make path relative, remove folder structure due replacing `/`
    with `_` and remove selected file extention `ext`.

    >>> simplify_testfile_names(('/c/abc/www/second.pdf', '/c/abc/def/first.pdf'))
    ('def_first', 'www_second')

    Determine relative files against an resource folder:

    >>> simplify_testfile_names(('/c/abc', '/c/abc/def/first.pdf'))
    ('def_first',)
    """
    # ensure to compute prefix correctly
    assert len(set(files)) > 1, 'require at least two unique items.'
    assert isinstance(files, (list, tuple)), f'unsupported type: {type(files)}'
    files = [utila.forward_slash(item) for item in files]
    prefix = utila.forward_slash(os.path.commonpath(files))
    # remove prefix
    files = [item.replace(prefix, '') for item in files]
    # remove empty path
    files = [item for item in files if item]
    # remove first slash
    files = [item[1:] if item[0] == '/' else item for item in files]
    # remove extension
    files = [item.replace(f'.{ext}', '') for item in files]
    # simplify name
    files = [item.replace('/', '_') for item in files]
    if sort:
        files = utila.files_sort(files)
    return tuple(files)


@contextlib.contextmanager
def increased_filecount(
    path: str = None,
    ext: str = None,
    mindiff: int = None,
    maxdiff: int = None,
):
    """Ensure that some files were created while yielded operation.

    Args:
        path(str): path to check for file creation, if path is None use cwd
        ext(str): look for a special file extention
        mindiff(int): minimal number of created files, if None: 1 is used
        maxdiff(int): maximal number of created files, if None: utila.INF is used
    Raises:
        AssertionError: if to few or less files are created
    Yields:
        None: to run file creation operation
    """
    if path is None:
        path = os.getcwd()
    assert os.path.exists(path), str(path)
    assert mindiff is None or mindiff >= 0, str(mindiff)
    assert maxdiff is None or maxdiff >= 0, str(maxdiff)
    pattern = '**/*.*' if ext is None else f'**/*.{ext}'
    with utila.chdir(path):
        before = list(glob.glob(pattern, recursive=True))
        yield
        after = list(glob.glob(pattern, recursive=True))
    mindiff = 1 if mindiff is None else mindiff
    maxdiff = utila.INF if maxdiff is None else maxdiff
    current = len(after) - len(before)
    assert mindiff <= current <= maxdiff, (
        f'mindiff: {mindiff} <= {len(after)-len(before)} <= maxdiff: {maxdiff}\n'
        f'{before}\n\n{after}')
