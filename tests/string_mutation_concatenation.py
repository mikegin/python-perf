


# large sizes performance switches
# setup:
class_names = ['primary', 'selected', 'active', 'medium']

# 1. mutation
def test_string_mutation(size):
    for i in range(size):
        ' '.join(map(lambda c: f'button--{c}', class_names))

# 2. concatenation
def test_string_concatenation(size):
    for i in range(size):
        ' '.join(map(lambda c: ' button--' + c, class_names))