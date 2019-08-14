# -*- coding: utf-8 -*-
# @Author: lcl1026504480
# @Date:   2019-08-14 17:46:54
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-08-14 17:46:54
import pstats
import cProfile

import pyximport
pyximport.install()

import calc_pi3

cProfile.runctx("calc_pi3.approx_pi()", globals(), locals(), "Profile.prof")

s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()
