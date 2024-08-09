def test_enum_string():
    position_str = {
        'TOP': 'TOP',
        'BOTTOM': 'BOTTOM'
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
            
def test_enum_string_long():
    position_str = {
        'TOP': 'TOP' * 1000,
        'BOTTOM': 'BOTTOM' * 1000
    }
    _ = 0
    for i in range(1000000):
        current = position_str['TOP'] if i % 2 == 0 else position_str['BOTTOM']
        if current == position_str['TOP']:
            _ += 1