# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-06-17 10:09:22
# @Last Modified by:   lenovouser
# @Last Modified time: 2019-06-17 10:09:22
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("fib.pyx", annotate=True),
)
