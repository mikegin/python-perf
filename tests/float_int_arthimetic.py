# https://www.reddit.com/r/Python/comments/ddootj/float_arithmetics_as_fast_or_even_faster_than_int/
def test_float_arithmetic():
    s = 1.0
    for i in range(0, 1000000):
        s += i

def test_int_arithmetic():
    s = 1
    for i in range(0, 1000000):
        s += i