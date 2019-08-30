# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-08-28 17:49:46
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-08-28 17:49:46


def myfunction(x, y=2):
    a = x - y
    return a + x * y


def _helper(a):
    return a + 1


class A:
    def __init__(self, b=0):
        self.a = 3
        self.b = b

    def foo(self, x):
        print(x + _helper(1.0))


import cython

if cython.compiled:
    print("Yep, I'm compiled.")
else:
    print("Just a lowly interpreted script.")
