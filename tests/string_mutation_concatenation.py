


# large sizes performance switches
# setup:
class_names = ['primary', 'selected', 'active', 'medium']
ITERATIONS = 1_000_000

# 1. mutation
def test_string_mutation():
    for i in range(ITERATIONS):
        ' '.join(map(lambda c: f'button--{c}', class_names))

# 2. concatenation
def test_string_concatenation():
    for i in range(ITERATIONS):
        ' '.join(map(lambda c: ' button--' + c, class_names))