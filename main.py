import time
import random
from functools import reduce
from hwcounter import Timer, count, count_end

def test_enum_string():
    position_str = {
        'TOP': 'TOP' * 1000,
        'BOTTOM': 'BOTTOM' * 1000
    }
    _ = 0
    for i in range(1000000):
        current = position_str['TOP'] if i % 2 == 0 else position_str['BOTTOM']
        if current == position_str['TOP']:
            _ += 1
            
def test_enum_int():
    position_int = {
        'TOP': 0,
        'BOTTOM': 1
    }

    _ = 0
    for i in range(1000000):
        current = position_int['TOP'] if i % 2 == 0 else position_int['BOTTOM']
        if current == position_int['TOP']:
            _ += 1

def add(a1, b1):
  return a1["a"] + a1["b"] + a1["c"] + a1["d"] + a1["e"] + b1["a"] + b1["b"] + b1["c"] + b1["d"] + b1["e"]

def test_shape_monomorphic():
    _ = 0
    o1 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o2 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o3 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o4 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o5 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 } # all shapes are equal
    
    result = 0
    for i in range(0, 1000000):
        result += add(o1, o2)
        result += add(o3, o4)
        result += add(o4, o5)
    return result

def test_shape_polymorphic():
    _ = 0
    o1 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o2 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o3 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o4 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o5 = { "b": 0, "a": 1, "c": 0, "d": 0, "e": 0 } # this shape is different
    
    result = 0
    for i in range(0, 1000000):
        result += add(o1, o2)
        result += add(o3, o4)
        result += add(o4, o5)
    return result
    
def test_shape_megamorphic():
    o1 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o2 = { "b": 0, "a": 1, "c": 0, "d": 0, "e": 0 }
    o3 = { "b": 0, "c": 0, "a": 1, "d": 0, "e": 0 }
    o4 = { "b": 0, "c": 0, "d": 0, "a": 1, "e": 0 }
    o5 = { "b": 0, "c": 0, "d": 0, "e": 0, "a": 1 } # all shapes are different

    result = 0
    for i in range(0, 1000000):
        result += add(o1, o2)
        result += add(o3, o4)
        result += add(o4, o5)
    return result

numbers = []
for i in range(0, 10_000):
    numbers.append(random.random())

def acc_add(a, x):
    return a + x

def functional_numbers():
    return reduce(acc_add, filter(lambda x: x % 2 == 0, map(lambda x: round(x * 10), numbers)))

def imperative_numbers():
    result = 0
    for i in numbers:
        n = round(i * 10)
        if n % 2 == 0:
            continue
        result += n
    return result



class Proxy:
    def __init__(self, obj):
        self._obj = obj
    
    def __getattr__(self, name):    
        return self._obj[name]
    
    def __getitem__(self, name):
        return self._obj[name]

def test_class_access_getattr():
    point = Proxy({'x': 10, 'y': 20})

    total = 0
    for i in range(100000):
        total += point.x

def test_class_access_getitem():
    point = Proxy({'x': 10, 'y': 20})

    total = 0
    for i in range(100000):
        total += point["x"]

def test_map_access():
    point = {'x': 10, 'y': 20}

    total = 0
    for i in range(100000):
        total += point["x"]
        
def test_direct_access():
    point = {'x': 10, 'y': 20}
    x = point['x']

    total = 0
    for i in range(100000):
        total += x
        



K = 1024
length = 1 * K * K

points = [{'x': 42, 'y': 0} for _ in range(length)]

shuffled_points = points[:]
random.shuffle(shuffled_points)

def test_sequential_access():
    _ = 0
    for point in points:
        _ += point['x']

def test_random_access():
    _ = 0
    for point in shuffled_points:
        _ += point['x']
        
        

# https://www.reddit.com/r/Python/comments/ddootj/float_arithmetics_as_fast_or_even_faster_than_int/
def float_arithmetic():
    s = 1.0
    for i in range(0, 1000000):
        s += i

def int_arithmetic():
    s = 1
    for i in range(0, 1000000):
        s += i
        




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





# setup
USERS_LENGTH = 1_000
by_id = {id: {'id': id, 'name': 'John'} for id in range(USERS_LENGTH)}

def test_large_obj_indirect():
    _ = 0

    for id in by_id:
        _ += by_id[id]['id']

def test_large_obj_direct():
    _ = 0
    
    for user in by_id.values():
        _ += user['id']



# setup:
key = 'requestId'
values = [42] * 100000

def test_without_eval():
    messages = []
    for value in values:
        messages.append({key: value})
    return messages

def test_with_eval():
    messages = []
    for value in values:
        message = eval(f'{{"{key}": {value}}}')
        messages.append(message)
    return messages





# setup:
class_names = ['primary', 'selected', 'active', 'medium']
ITERATIONS = 1_000_000

# 1. mutation
def test_string_mutation():
    for i in range(ITERATIONS):
        ' '.join(map(lambda c: f'button--{c}', class_names))

# 2. concatenation
def test_string_concatenation():
    for i in range(ITERATIONS):
        ' '.join(map(lambda c: ' button--' + c, class_names))









descriptions = ['apples', 'oranges', 'bananas', 'seven']
some_tags = {
    'apples': '::promotion::',
}
no_tags = {}

def is_empty(o):
    return len(o) == 0

def products_to_string(description, tags):
    result = ''
    for product in description:
        result += product
        if product in tags:
            result += tags[product]
        result += ', '
    return result

def products_to_string_specialized(description, tags):
    if is_empty(tags):
        result = ''
        for product in description:
            result += product + ', '
        return result
    else:
        result = ''
        for product in description:
            result += product
            if product in tags:
                result += tags[product]
            result += ', '
        return result

def test_not_specialized():
    for _ in range(1_000_000):
        products_to_string(descriptions, some_tags)
        products_to_string(descriptions, no_tags)

def test_specialized():
    for _ in range(1_000_000):
        products_to_string_specialized(descriptions, some_tags)
        products_to_string_specialized(descriptions, no_tags)





with Timer() as t:
    time.sleep(1)

cycles_per_second = t.cycles

# test_enum_string, test_enum_int, test_shape_monomorphic, test_shape_polymorphic, test_shape_megamorphic, functional_numbers, imperative_numbers, test_class_access, test_map_access, test_direct_access
for test in [test_not_specialized, test_specialized]:
    run_count = 10
    # avg = 0
    avg_cycles = 0
    for i in range(0, run_count):
        # t = time.perf_counter_ns()
        # test()
        # tt = time.perf_counter_ns() - t
        # avg += tt
        
        with Timer() as t:
            test()
        avg_cycles += t.cycles
    # avg /= run_count
    # print(f"{test.__name__} avg ms:", avg / 1000 / 1000)
    avg_cycles /= run_count
    print(f'{test.__name__}: avg cycles = {avg_cycles}, time taken = {avg_cycles / cycles_per_second * 1000} ms')

    