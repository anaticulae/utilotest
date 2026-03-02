# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2019-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

# import sys
# import threading

# import pytest
# import utilo

# import utilotest

# PACKAGE = """\
# import setuptools
# setuptools.setup(
#     name='%s',
#     packages=['%s'],
# )
# """

# linux = not sys.platform.startswith("win")

# class TestClass:

#     LOCK = threading.Lock()

#     @utilotest.nonvirtual
#     @utilotest.longrun
#     def test_clean_install(_, td):
#         if linux:
#             pytest.skip('enable later')
#         with TestClass.LOCK:
#             package = 'dorimifasa'
#             td.mkdir(package)
#             utilo.file_create(
#                 td.tmpdir.join('setup.py'),
#                 PACKAGE % (package, package),
#             )
#             utilo.run('python setup.py build')
#             utilotest.clean_install(
#                 td.tmpdir,
#                 'dorimifasa',
#             )
#         # @utilotest.nonvirtual
#         # @utilotest.longrun
#         # def test_install_and_run(self, td):  # pylint:disable=R0201
#         with TestClass.LOCK:
#             package = 'dorimifasamore'
#             # td.mkdir(package)
#             # utilo.file_create(
#             #     td.tmpdir.join('setup.py'),
#             #     PACKAGE % (package, package),
#             # )
#             utilo.run('python setup.py build')
#             utilotest.install_and_run(
#                 root=td.tmpdir,
#                 package=package,
#                 executable='power',  # not the installed one
#             )
