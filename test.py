def print_pairing_dict(pdict):
    for student, pairs in pdict.items():
        print(student)
        for name, occ in pairs.items():
            print('\t' + name + ': ', occ)

def run_test(db_name, student_arr):
    pairing_dict = read_dict(db_name)
    for _ in range(1000):
        print_and_update_pairs(pairing_dict)
    print_pairing_dict(pairing_dict)
