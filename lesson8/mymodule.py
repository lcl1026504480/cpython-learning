# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-08-29 17:42:43
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-08-29 17:42:43
# mymodule.py

import cython

# override with Python import if not in compiled code
if not cython.compiled:
    print(True)
    from math import sin

# calls sin() from math.h when compiled with Cython and math.sin() in Python
print(_sin(0))
