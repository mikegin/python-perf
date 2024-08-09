
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