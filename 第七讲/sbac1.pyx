# -*- coding: ASCII -*-


cdef char char_val = 'A'
assert char_val == 65   # ASCII encoded byte value of 'A'
# print(char_val)
# print( < bytes > char_val )
cdef bytes py_byte_string
py_byte_string = char_val
print(py_byte_string)
