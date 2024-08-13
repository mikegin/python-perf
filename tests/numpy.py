import numpy as np

def test_regular_float_sum(size):
    s = 1.0
    buffer = [float(i) for i in range(size)]
    for i in buffer:
        s += i

def test_numpy_float_sum(size):
    s = 1.0
    buffer = [float(i) for i in range(size)]
    s += np.sum(buffer, dtype=np.float64)

def test_builtin_float_sum(size):
    s = 1.0
    buffer = [float(i) for i in range(size)]
    s += sum(buffer)