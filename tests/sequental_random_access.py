
K = 1024
length = 1 * K * K

points = [{'x': 42, 'y': 0} for _ in range(length)]

shuffled_points = points[:]
random.shuffle(shuffled_points)

def test_sequential_access():
    _ = 0
    for point in points:
        _ += point['x']

def test_random_access():
    _ = 0
    for point in shuffled_points:
        _ += point['x']