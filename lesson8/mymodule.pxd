# mymodule.pxd

# declare a C function as "cpdef" to export it to the module
cdef extern from "math.h":
    cpdef double _sin "sin" (double x)
