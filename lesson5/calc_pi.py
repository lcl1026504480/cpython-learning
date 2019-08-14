# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-08-14 09:21:11
# @Last Modified by:   lenovouser
# @Last Modified time: 2019-08-14 09:21:11


def recip_square(i):
    return 1. / i ** 2


def approx_pi(n=10000000):
    val = 0.
    for k in range(1, n + 1):
        val += recip_square(k)
    return (6 * val) ** .5
