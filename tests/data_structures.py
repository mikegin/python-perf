'''
Interesting findings:
Ratio of improvement with increase to number of user ids decreases
At 1_000, improvement was 2x
At 1_000_000 improvement looks closer to 1.5x
'''

# setup
user_ids = []
admin_ids_list = []
admin_ids_set = set()

def init(size):
    user_ids = list(range(size))
    admin_ids_list = user_ids[:10]
    admin_ids_set = set(admin_ids_list)

def test_list(size):
    _ = 0
    for i in range(len(user_ids)):
        if user_ids[i] in admin_ids_list:
            _ += 1

def test_set(size):
    _ = 0
    for i in range(len(user_ids)):
        if user_ids[i] in admin_ids_set:
            _ += 1


setup = {
    "init": init,
    "tests": [test_list, test_set]
}