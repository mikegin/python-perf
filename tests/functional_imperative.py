import random
from functools import reduce

numbers = []
for i in range(0, 10_000):
    numbers.append(random.random())

def acc_add(a, x):
    return a + x

def test_functional_numbers():
    return reduce(acc_add, filter(lambda x: x % 2 == 0, map(lambda x: round(x * 10), numbers)))

def test_imperative_numbers():
    result = 0
    for i in numbers:
        n = round(i * 10)
        if n % 2 == 0:
            continue
        result += n
    return result