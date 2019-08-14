# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-08-14 18:05:25
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-08-14 18:05:25


def approx_pi(long long n=10000000):
    cdef double val = 0.
    cdef long long k
    for k in range(1, n + 1):
        val += 1. / (k * k)
    return (6 * val) ** .5
