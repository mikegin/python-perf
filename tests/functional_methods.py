import random
from functools import reduce

def get_numbers(size):
    numbers = []
    for i in range(0, size):
        numbers.append(random.random())
    
    return numbers

def acc_add(a, x):
    return a + x

def test_functional_numbers(size):
    return reduce(acc_add, filter(lambda x: x % 2 == 0, map(lambda x: round(x * 10), get_numbers(size))))

def test_imperative_numbers(size):
    result = 0
    for i in get_numbers(size):
        n = round(i * 10)
        if n % 2 == 0:
            continue
        result += n
    return result


## Just map
# def test_functional_numbers(size):
#     return list(map(lambda x: round(x * 10), get_numbers(size)))

# def test_imperative_numbers(size):
#     result = []
#     for i in get_numbers(size):
#         result.append(round(i * 10))
#     return result


## Just map + filter
# def test_functional_numbers(size):
#     return list(filter(lambda x: x % 2 == 0, map(lambda x: round(x * 10), get_numbers(size))))

# def test_imperative_numbers(size):
#     result = []
#     for i in get_numbers(size):
#         n = round(i * 10)
#         if n % 2 == 0:
#             continue
#         result.append(n)
#     return result