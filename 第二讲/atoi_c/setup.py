# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-06-17 20:05:28
# @Last Modified by:   lenovouser
# @Last Modified time: 2019-06-17 20:05:28
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("atoi_c.pyx", annotate=True),
)
