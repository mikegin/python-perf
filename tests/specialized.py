'''
Interesting Notes:
The specialized case here runs slower as 
'''

descriptions = ['apples', 'oranges', 'bananas', 'seven']
some_tags = {
    'apples': '::promotion::',
}
no_tags = {}

def is_empty(o):
    return len(o) == 0

def products_to_string(description, tags):
    result = ''
    for product in description:
        result += product
        if product in tags:
            result += tags[product]
        result += ', '
    return result

def products_to_string_specialized(description, tags):
    if is_empty(tags):
        result = ''
        for product in description:
            result += product + ', '
        return result
    else:
        result = ''
        for product in description:
            result += product
            if product in tags:
                result += tags[product]
            result += ', '
        return result

def test_not_specialized(size):
    for _ in range(size):
        products_to_string(descriptions, some_tags)
        products_to_string(descriptions, no_tags)

def test_specialized(size):
    for _ in range(size):
        products_to_string_specialized(descriptions, some_tags)
        products_to_string_specialized(descriptions, no_tags)