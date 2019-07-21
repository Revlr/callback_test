#! python2.7
from ctypes import *

def py_sum_func(a, b):
	print "run py_sum_func", a, b
	print "a + b = ", a + b
	return 0

SUMFUNC = WINFUNCTYPE(c_int, c_int, c_int)
#WINFUNCTYPE(restype, arg1 type, arg2 type, ...)
#WINFUNCTYPE make function fastcall
#if you want cdecl function, use CFUNCTYPE

sum_func = SUMFUNC(py_sum_func)
#function type setting
#make py_sum_func into ctype funtion pointer

dll = windll.LoadLibrary('dllTest.dll')
dll.foo(sum_func, 2, 4)
