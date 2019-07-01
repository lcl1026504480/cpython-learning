# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-17 20:46:43
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-17 20:47:00
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("math_c.pyx", annotate=True),
)