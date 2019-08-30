# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-08-30 15:17:04
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-08-30 17:52:30
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("pythonarray4.pyx", annotate=True),
)