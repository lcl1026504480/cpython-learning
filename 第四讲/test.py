# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-06-30 17:21:01
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-07-01 17:56:03
import pyximport
pyximport.install()
import integrate


class MyPolynomial(integrate.Function):
    def evaluate(self, x):
        return 2 * x * x + 3 * x - 10


print(integrate.integrate(MyPolynomial(), 0, 1, 10000))
