
class Proxy:
    def __init__(self, obj):
        self._obj = obj
    
    def __getattr__(self, name):    
        return self._obj[name]
    
    def __getitem__(self, name):
        return self._obj[name]

def test_class_access_getattr():
    point = Proxy({'x': 10, 'y': 20})

    total = 0
    for i in range(100000):
        total += point.x

def test_class_access_getitem():
    point = Proxy({'x': 10, 'y': 20})

    total = 0
    for i in range(100000):
        total += point["x"]

def test_map_access():
    point = {'x': 10, 'y': 20}

    total = 0
    for i in range(100000):
        total += point["x"]
        
def test_direct_access():
    point = {'x': 10, 'y': 20}
    x = point['x']

    total = 0
    for i in range(100000):
        total += x