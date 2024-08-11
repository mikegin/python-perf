
def get_large_obj(size):
    
    by_id = {id: {'id': id, 'name': 'John'} for id in range(size)}
    
    return by_id

def test_large_obj_indirect(size):
    _ = 0

    by_id = get_large_obj(size)
    
    for id in by_id:
        _ += by_id[id]['id']

def test_large_obj_direct(size):
    _ = 0
    
    by_id = get_large_obj(size)
    
    for user in by_id.values():
        _ += user['id']