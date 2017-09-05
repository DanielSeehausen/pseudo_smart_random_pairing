def true_random_assign_pairs(arr):
    print([arr.pop(random.randrange(len(arr))) for _ in range(2)])
    if len(arr) > 1:
        random_assign(arr)
    else:
        print(arr)

def get_all_pairs(matchee, arr):
    return {matcher: 0 for matcher in arr if matchee != matcher}
