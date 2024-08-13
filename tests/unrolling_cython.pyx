# optimized.pyx

# Add necessary imports
import cython
import numpy as np
from libc.stdlib cimport malloc, free
from cython.view cimport array

@cython.boundscheck(False)
@cython.wraparound(False)
def test_cython_sum_list_unrolled_0(int size):
    cdef double total = 0
    cdef int i
    cdef double[:] numbers = np.arange(size, dtype=np.float64)
    
    for i in range(size):
        total += numbers[i]
    return total

@cython.boundscheck(False)
@cython.wraparound(False)
def test_cython_sum_list_unrolled_2(int size):
    cdef double total1 = 0, total2 = 0
    cdef int i, n
    cdef double[:] numbers = np.arange(size, dtype=np.float64)
    n = size
    
    for i in range(0, n - 1, 2):
        total1 += numbers[i]
        total2 += numbers[i + 1]
    
    if n % 2 != 0:
        total1 += numbers[n-1]
    
    return total1 + total2

@cython.boundscheck(False)
@cython.wraparound(False)
def test_cython_sum_list_unrolled_4(int size):
    cdef double total1 = 0, total2 = 0, total3 = 0, total4 = 0
    cdef int i, n
    cdef double[:] numbers = np.arange(size, dtype=np.float64)
    n = size
    
    for i in range(0, n - 3, 4):
        total1 += numbers[i]
        total2 += numbers[i + 1]
        total3 += numbers[i + 2]
        total4 += numbers[i + 3]
    
    for i in range(n - (n % 4), n):
        total1 += numbers[i]
    
    return total1 + total2 + total3 + total4

@cython.boundscheck(False)
@cython.wraparound(False)
def test_cython_sum_list_unrolled_8(int size):
    cdef double total1 = 0, total2 = 0, total3 = 0, total4 = 0
    cdef double total5 = 0, total6 = 0, total7 = 0, total8 = 0
    cdef int i, n
    cdef double[:] numbers = np.arange(size, dtype=np.float64)
    n = size
    
    for i in range(0, n - 7, 8):
        total1 += numbers[i]
        total2 += numbers[i + 1]
        total3 += numbers[i + 2]
        total4 += numbers[i + 3]
        total5 += numbers[i + 4]
        total6 += numbers[i + 5]
        total7 += numbers[i + 6]
        total8 += numbers[i + 7]
    
    for i in range(n - (n % 8), n):
        total1 += numbers[i]
    
    return total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8

@cython.boundscheck(False)
@cython.wraparound(False)
def test_cython_sum_list_unrolled_16(int size):
    cdef double total1 = 0, total2 = 0, total3 = 0, total4 = 0
    cdef double total5 = 0, total6 = 0, total7 = 0, total8 = 0
    cdef double total9 = 0, total10 = 0, total11 = 0, total12 = 0
    cdef double total13 = 0, total14 = 0, total15 = 0, total16 = 0
    cdef int i, n
    cdef double[:] numbers = np.arange(size, dtype=np.float64)
    n = size
    
    for i in range(0, n - 15, 16):
        total1 += numbers[i]
        total2 += numbers[i + 1]
        total3 += numbers[i + 2]
        total4 += numbers[i + 3]
        total5 += numbers[i + 4]
        total6 += numbers[i + 5]
        total7 += numbers[i + 6]
        total8 += numbers[i + 7]
        total9 += numbers[i + 8]
        total10 += numbers[i + 9]
        total11 += numbers[i + 10]
        total12 += numbers[i + 11]
        total13 += numbers[i + 12]
        total14 += numbers[i + 13]
        total15 += numbers[i + 14]
        total16 += numbers[i + 15]
    
    for i in range(n - (n % 16), n):
        total1 += numbers[i]
    
    return (total1 + total2 + total3 + total4 + total5 + total6 + total7 + total8 +
            total9 + total10 + total11 + total12 + total13 + total14 + total15 + total16)
