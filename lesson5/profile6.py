# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-08-15 09:52:37
# @Last Modified by:   lenovouser
# @Last Modified time: 2019-08-15 09:52:37
import pstats
import cProfile

import pyximport
pyximport.install()

import calc_pi6

cProfile.runctx("calc_pi6.approx_pi()", globals(), locals(), "Profile.prof")

s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()
