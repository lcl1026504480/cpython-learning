# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-08-29 19:19:58
# @Last Modified by:   lenovouser
# @Last Modified time: 2019-08-30 09:59:13
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("convolve4.pyx", annotate=True),
)
