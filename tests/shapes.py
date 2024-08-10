def add(a1, b1):
  return a1["a"] + a1["b"] + a1["c"] + a1["d"] + a1["e"] + b1["a"] + b1["b"] + b1["c"] + b1["d"] + b1["e"]

def test_shape_monomorphic(iterations):
    _ = 0
    o1 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o2 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o3 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o4 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o5 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 } # all shapes are equal
    
    result = 0
    for i in range(iterations):
        result += add(o1, o2)
        result += add(o3, o4)
        result += add(o4, o5)
    return result

def test_shape_polymorphic(iterations):
    _ = 0
    o1 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o2 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o3 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o4 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o5 = { "b": 0, "a": 1, "c": 0, "d": 0, "e": 0 } # this shape is different
    
    result = 0
    for i in range(iterations):
        result += add(o1, o2)
        result += add(o3, o4)
        result += add(o4, o5)
    return result
    
def test_shape_megamorphic(iterations):
    o1 = { "a": 1, "b": 0, "c": 0, "d": 0, "e": 0 }
    o2 = { "b": 0, "a": 1, "c": 0, "d": 0, "e": 0 }
    o3 = { "b": 0, "c": 0, "a": 1, "d": 0, "e": 0 }
    o4 = { "b": 0, "c": 0, "d": 0, "a": 1, "e": 0 }
    o5 = { "b": 0, "c": 0, "d": 0, "e": 0, "a": 1 } # all shapes are different

    result = 0
    for i in range(iterations):
        result += add(o1, o2)
        result += add(o3, o4)
        result += add(o4, o5)
    return result