# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-17 15:21:54
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-17 15:22:31
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("primes_cpp.pyx", annotate=True),
)
