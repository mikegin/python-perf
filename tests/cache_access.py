import numpy as np
import random

'''
Interesting Notes:
On initial (low) iterations, the first test to run is usually slower. This may be due to page faults happening once memory is actually mapped by the OS.
'''

# These are approximate sizes to fit in those caches. If you don't get the
# same results on your machine, it might be because your sizes differ.

L1 = 256 * 1000 # 544KiB L1 on my machine
L2 = 2 * 1000 * 1000 # 11.5 MiB on my machine 
L3 = 14 * 1000 * 1000 # 24 MiB on my machine
RAM = 5 * 1000 * 1000 * 1000 # 32 GiB on my machine

# We'll be accessing the same buffer for all test cases, but we'll
# only be accessing the first 0 to `L1` entries in the first case,
# 0 to `L2` in the second, etc.
buffer = np.full(RAM, 42, dtype=np.int8)

# Function to generate a random index
def get_random(max_value):
    return random.randint(0, max_value - 1)

def test_l1(iterations):
    r = 0
    for _ in range(iterations):
        r += buffer[get_random(L1)]

def test_l2(iterations):
    r = 0
    for _ in range(iterations):
        r += buffer[get_random(L2)]

def test_l3(iterations):
    r = 0
    for _ in range(iterations):
        r += buffer[get_random(L3)]

def test_ram(iterations):
    r = 0
    for _ in range(iterations):
        r += buffer[get_random(RAM)]