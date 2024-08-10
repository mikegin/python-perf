
class Proxy:
    def __init__(self, obj):
        self._obj = obj
    
    def __getattr__(self, name):    
        return self._obj[name]
    
    def __getitem__(self, name):
        return self._obj[name]

def test_class_access_getattr(iterations):
    point = Proxy({'x': 10, 'y': 20})

    total = 0
    for i in range(iterations):
        total += point.x

def test_class_access_getitem(iterations):
    point = Proxy({'x': 10, 'y': 20})

    total = 0
    for i in range(iterations):
        total += point["x"]

def test_map_access(iterations):
    point = {'x': 10, 'y': 20}

    total = 0
    for i in range(iterations):
        total += point["x"]
        
def test_direct_access(iterations):
    point = {'x': 10, 'y': 20}
    x = point['x']

    total = 0
    for i in range(iterations):
        total += x