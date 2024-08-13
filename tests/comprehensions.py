

def test_comprehensions(size):
    result = [i for i in range(size)]
    
    return result

def test_regular_loops(size):
    result = []
    for i in range(size):
        result.append(i)
    
    return result