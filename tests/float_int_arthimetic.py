# https://www.reddit.com/r/Python/comments/ddootj/float_arithmetics_as_fast_or_even_faster_than_int/
def test_float_arithmetic(size):
    s = 1.0
    buffer = [float(i) for i in range(size)]
    for i in buffer:
        s += i

def test_int_arithmetic(size):
    s = 1
    buffer = [int(i) for i in range(size)]
    for i in buffer:
        s += i