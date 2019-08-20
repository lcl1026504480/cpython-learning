# distutils: language = c++

from libcpp.string cimport string


def get_bytes():
    py_unicode_string = "我爱中国"
    cdef string cpp_string = py_unicode_string.encode('UTF-8')
    return cpp_string
