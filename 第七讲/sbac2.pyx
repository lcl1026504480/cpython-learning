# cdef Py_UNICODE uchar_val = u'A'
# cdef Py_UCS4 uchar_val = u'A'
# assert uchar_val == 65  # character point value of u'A'
# print(uchar_val)
cdef Py_UCS4 uchar_val = u'A'
print( < long > uchar_val )
