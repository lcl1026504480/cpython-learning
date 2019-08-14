# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-07-22 11:45:20
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-07-22 11:45:20
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(n.pyx", annotate=True),
)
