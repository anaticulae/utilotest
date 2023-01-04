# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import utila

LOG_FILES = utila.splitlines("""
done
failed
generated.log
inprogress
""")
OUTPUTDIR = '__traceback__'


@utila.saveme
def main():
    cwd = os.getcwd()
    utila.log(f'collect: {cwd}')
    files = utila.file_list(
        path=cwd,
        absolute=True,
    )
    files = [item for item in files if with_error(item)]
    outdir = os.path.join(cwd, OUTPUTDIR)
    utila.log(f'write to: {outdir}')
    os.makedirs(outdir, exist_ok=True)
    for index, item in enumerate(files):
        utila.log(item)
        index = str(index).zfill(2)
        outpath = os.path.join(outdir, index)
        utila.file_copy(item, outpath, timestamp=True)
    return utila.SUCCESS


TRACEBACK = utila.compiles(r"""
    (
        Traceback[ ]\(most[ ]recent[ ]call[ ]last\)\:|
        error\:[ ]unrecognized[ ]arguments\:
    )
""")


def with_error(path) -> bool:
    # file name with extension
    filename = utila.file_name(path, ext=True).lower()
    if OUTPUTDIR in path:
        return False
    if filename not in LOG_FILES:
        return False
    content = utila.file_read(path)
    if TRACEBACK.search(content):
        # detect error inside log file
        return True
    return False
