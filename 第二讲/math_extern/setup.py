# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-17 21:30:37
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-17 21:30:55
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("math_c_extern.pyx", annotate=True),
)