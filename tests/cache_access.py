import numpy as np
import random

# setup
KB = 1024
MB = 1024 * KB

# These are approximate sizes to fit in those caches. If you don't get the
# same results on your machine, it might be because your sizes differ.
# L1 = 256 * KB
L1 = 544 * 1000 # 544KiB
L2 = 11 * 1000 * 1000 # 11 MiB
L3 = 24 * 1000 * 1000 # 24 MiB
RAM = 16 * 1000 * 1000 * 1000 # 16 GiB

# We'll be accessing the same buffer for all test cases, but we'll
# only be accessing the first 0 to `L1` entries in the first case,
# 0 to `L2` in the second, etc.
buffer = np.full(RAM, 42, dtype=np.int8)

# Function to generate a random index
def get_random(max_value):
    return random.randint(0, max_value - 1)

def test_l1():
    r = 0
    for _ in range(100000):
        r += buffer[get_random(L1)]

def test_l2():
    r = 0
    for _ in range(100000):
        r += buffer[get_random(L2)]

def test_l3():
    r = 0
    for _ in range(100000):
        r += buffer[get_random(L3)]

def test_ram():
    r = 0
    for _ in range(100000):
        r += buffer[get_random(RAM)]