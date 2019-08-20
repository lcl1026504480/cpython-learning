# define a global name for whatever char type is used in the module
ctypedef unsigned char char_type

cpdef char_type[:] _chars(s):
    if isinstance(s, unicode):
        # encode to the specific encoding used inside of the module
        s1 = ( < unicode > s).encode('utf8')
    return s1
