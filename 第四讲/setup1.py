# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-30 17:42:16
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-30 17:42:41
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("sin_of_square.pyx", annotate=True),
)
