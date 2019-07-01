# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-06-20 15:57:53
# @Last Modified by:   lenovouser
# @Last Modified time: 2019-06-23 16:51:44
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([Extension("sin_of_square", ["sin_of_square.pyx"])])
)
