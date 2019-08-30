# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-08-29 17:11:37
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-08-29 17:17:06
import cython
cython.declare(x=cython.int, x_ptr=cython.p_int)
x = 5
x_ptr = cython.address(x)
cython.declare(n=cython.longlong)
print(cython.sizeof(cython.longlong))
n = 400
print(cython.sizeof(n))
MyStruct = cython.struct(x=cython.int, y=cython.int, data=cython.double)
a = cython.declare(MyStruct)
T = cython.typedef(cython.p_int)   # ctypedef int* T
# t1 = cython.cast(T, t)
# t2 = cython.cast(T, t, typecheck=True)
