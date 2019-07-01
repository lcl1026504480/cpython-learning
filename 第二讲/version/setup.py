# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-17 20:40:31
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-17 20:42:38
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("version.pyx", annotate=True),
)
