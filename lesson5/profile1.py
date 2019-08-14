# -*- coding: utf-8 -*-
# @Author: lenovouser
# @Date:   2019-08-14 09:21:42
# @Last Modified by:   lcl1026504480
# @Last Modified time: 2019-08-14 10:29:40
import pstats
import cProfile
# import profile
import calc_pi


cProfile.runctx("calc_pi.approx_pi()", globals(), locals(), "Profile.prof")

s = pstats.Stats("Profile.prof")
s.strip_dirs().sort_stats("time").print_stats()
