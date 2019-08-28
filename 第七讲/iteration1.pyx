# cdef char * c_string = b"Hello to A C-string's world"

# cdef char c
# for c in c_string[:11]:
#     if c == 'A':
#         print("Found the letter A")
cdef unicode ustring = u'Hello world'

# NOTE: no typing required for 'uchar' !
for uchar in ustring:
    if uchar == u'A':
        print("Found the letter A")