
# setup:

key = 'requestId'

def get_values(size):
    values = [42] * 100000
    
    return values

def test_without_eval(size):
    messages = []
    
    for value in get_values(size):
        messages.append({key: value})
    return messages

def test_with_eval(size):
    messages = []
    for value in get_values(size):
        message = eval(f'{{"{key}": {value}}}')
        messages.append(message)
    return messages