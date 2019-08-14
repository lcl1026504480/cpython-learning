# cython: profile=True

# calc_pi3.pyx

cdef inline double recip_square(long long i):
    return 1. / (i * i)


def approx_pi(long long n=10000000):
    cdef double val = 0.
    cdef int k
    for k in range(1, n + 1):
        val += recip_square(k)
    return (6 * val) ** .5
