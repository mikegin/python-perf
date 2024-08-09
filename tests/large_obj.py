
# setup
USERS_LENGTH = 1_000
by_id = {id: {'id': id, 'name': 'John'} for id in range(USERS_LENGTH)}

def test_large_obj_indirect():
    _ = 0

    for id in by_id:
        _ += by_id[id]['id']

def test_large_obj_direct():
    _ = 0
    
    for user in by_id.values():
        _ += user['id']