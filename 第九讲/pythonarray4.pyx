from cpython cimport array
import array

cdef array.array int_array_template = array.array('i', [])
cdef array.array newarray

# create an array with 3 elements with same type as template
newarray = array.clone(int_array_template, 3, zero=True)
# from cpython cimport array
# import array

# extend a with b, resize as needed
cdef array.array a = array.array('i', [1, 2, 3])
cdef array.array b = array.array('i', [4, 5, 6])

array.extend(a, b)


def main():
    # print("in .pyx")
    print(newarray, a, b)
    array.resize(a, len(a) - len(b))


# resize a, leaving just original three elements
# main()
