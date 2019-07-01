# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-17 20:39:43
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-06-17 20:39:43
from cpython.version cimport PY_VERSION_HEX

# Python version >= 3.2 final ?
print(PY_VERSION_HEX >= 0x030200F0)
