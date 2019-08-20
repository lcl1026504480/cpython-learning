# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-08-19 17:03:31
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-08-20 13:23:10
from distutils.core import setup
from Cython.Build import cythonize
setup(
    ext_modules=cythonize("cppeg3.pyx", annotate=True),
)
# setup(
#     ext_modules=cythonize("cppeg2.pyx", annotate=True),
# )

# setup(
#     ext_modules=cythonize("cppeg1.pyx", annotate=True),
# )

# setup(
#     ext_modules=cythonize("encodetotext.pyx", annotate=True),
# )
