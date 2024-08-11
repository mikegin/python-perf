def test_compare_string(iterations):
    position_str = {
        'TOP': 'TOP',
        'BOTTOM': 'BOTTOM'
    }
    _ = 0
    for i in range(iterations):
        current = position_str['TOP'] if i % 2 == 0 else position_str['BOTTOM']
        if current == position_str['TOP']:
            _ += 1
            
def test_compare_int(iterations):
    position_int = {
        'TOP': 0,
        'BOTTOM': 1
    }

    _ = 0
    for i in range(iterations):
        current = position_int['TOP'] if i % 2 == 0 else position_int['BOTTOM']
        if current == position_int['TOP']:
            _ += 1

def test_compare_float(iterations):
    position_int = {
        'TOP': 0.0,
        'BOTTOM': 1.0
    }

    _ = 0
    for i in range(iterations):
        current = position_int['TOP'] if i % 2 == 0 else position_int['BOTTOM']
        if current == position_int['TOP']:
            _ += 1
            
def test_compare_string_long(iterations):
    position_str = {
        'TOP': 'TOP' * 1000,
        'BOTTOM': 'TOP' * 1000 + 'B'
    }
    _ = 0
    for i in range(iterations):
        current = position_str['TOP'] if i % 2 == 0 else position_str['BOTTOM']
        if current == position_str['TOP']:
            _ += 1