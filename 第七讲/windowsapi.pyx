import sys
cdef extern from "windows.h":

    ctypedef Py_UNICODE WCHAR
    ctypedef const WCHAR * LPCWSTR
    ctypedef void * HWND

    int MessageBoxW(HWND hWnd, LPCWSTR lpText, LPCWSTR lpCaption, int uType)

title = u"Windows Interop Demo - Python %d.%d.%d" % sys.version_info[:3]
MessageBoxW(NULL, u"Hello Cython \u263a", title, 0)
