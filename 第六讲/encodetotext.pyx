# encodetotext.pyx
def main():
    py_unicode_string = "我爱中国"
    # py_byte_string = py_unicode_string.encode('UTF-8')
    # cdef char * c_string = py_byte_string
    cdef char * c_string = py_unicode_string.encode('UTF-8')
    print(c_string)
