'''
Interesting findings:
Ratio of improvement with increase to number of user ids decreases
At 1_000, improvement was 2x
At 1_000_000 improvement looks closer to 1.5x
'''

def init(size):
    user_ids = list(range(size))
    admin_ids_list = user_ids[:10]
    admin_ids_set = set(admin_ids_list)
    
    return user_ids, admin_ids_list, admin_ids_set

def test_list(size):
    user_ids, admin_ids_list, admin_ids_set = init(size)
    
    _ = 0
    for i in range(len(user_ids)):
        if user_ids[i] in admin_ids_list:
            _ += 1

def test_set(size):
    user_ids, admin_ids_list, admin_ids_set = init(size)
    
    _ = 0
    for i in range(len(user_ids)):
        if user_ids[i] in admin_ids_set:
            _ += 1
