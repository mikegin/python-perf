import random

def init(size):
    points = [{'x': 42, 'y': 0} for _ in range(size)]

    shuffled_points = points[:]
    random.shuffle(shuffled_points)
    
    return points, shuffled_points

def test_sequential_access(size):
    points, shuffled_points = init(size)
    
    _ = 0
    for point in points:
        _ += point['x']

def test_random_access(size):
    points, shuffled_points = init(size)
    
    _ = 0
    for point in shuffled_points:
        _ += point['x']