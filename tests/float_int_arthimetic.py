# https://www.reddit.com/r/Python/comments/ddootj/float_arithmetics_as_fast_or_even_faster_than_int/
def test_float_arithmetic(size):
    s = 1.0
    for i in range(size):
        s += i

def test_int_arithmetic(size):
    s = 1
    for i in range(size):
        s += i