# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utilo

LOG_FILES = utilo.splitlines("""
done
failed
generated.log
inprogress
""")
OUTPUTDIR = '__traceback__'


@utilo.saveme
def main():
    cwd = os.getcwd()
    utilo.log(f'collect: {cwd}')
    files = utilo.file_list(
        path=cwd,
        absolute=True,
    )
    files = [item for item in files if with_error(item)]
    outdir = os.path.join(cwd, OUTPUTDIR)
    utilo.log(f'write to: {outdir}')
    os.makedirs(outdir, exist_ok=True)
    for index, item in enumerate(files):
        utilo.log(item)
        index = str(index).zfill(2)
        outpath = os.path.join(outdir, index)
        utilo.file_copy(item, outpath, timestamp=True)
    return utilo.SUCCESS


TRACEBACK = utilo.compiles(r"""
    (
        Traceback[ ]\(most[ ]recent[ ]call[ ]last\)\:|
        error\:[ ]unrecognized[ ]arguments\:
    )
""")


def with_error(path) -> bool:
    # file name with extension
    filename = utilo.file_name(path, ext=True).lower()
    if OUTPUTDIR in path:
        return False
    if filename not in LOG_FILES:
        return False
    content = utilo.file_read(path)
    if TRACEBACK.search(content):
        # detect error inside log file
        return True
    return False
