# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-08-21 20:54:18
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-08-28 16:19:42
from distutils.core import setup
from Cython.Build import cythonize

# setup(
#     ext_modules=cythonize("autoutf8.pyx", annotate=True),
# )
# setup(
#     ext_modules=cythonize("autoascii.pyx", annotate=True),
# )
# setup(
#     ext_modules=cythonize("autoua.pyx", annotate=True),
# )
# setup(
#     ext_modules=cythonize("sbac1.pyx", annotate=True),
# )
# setup(
#     ext_modules=cythonize("sbac2.pyx", annotate=True),
# )
# setup(
#     ext_modules=cythonize("narrowunicode.pyx", annotate=True),
# )
# setup(
#     ext_modules=cythonize("iteration1.pyx", annotate=True),
# )
# setup(
#     ext_modules=cythonize("iteration2.pyx", annotate=True),
# )
# setup(
#     ext_modules=cythonize("windowsapi.pyx", annotate=True),
# )

setup(
    ext_modules=cythonize("memorymalloc2.pyx", annotate=True),
)



