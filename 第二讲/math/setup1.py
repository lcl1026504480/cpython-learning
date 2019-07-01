# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-17 20:56:00
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-17 20:56:00
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [
    Extension("math_c",
              sources=["math_c.pyx"],
              libraries=["m"]  # Unix-like specific
              )
]

setup(name="Demos",
      ext_modules=cythonize(ext_modules))
