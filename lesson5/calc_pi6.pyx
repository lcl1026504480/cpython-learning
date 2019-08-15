
from libc.math cimport sqrt


def approx_pi(long long n=10000000):
    cdef double val = 0.
    cdef long long k
    for k in range(1, n + 1):
        val += 1. / (k * k)
    return sqrt(6 * val)
