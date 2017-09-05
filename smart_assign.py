#!/usr/bin/env python3

import random, os.path, sys, json
from students import student_arr
from pathlib import Path

db_name = os.path.dirname(os.path.realpath(__file__)) + '/pairing_db.json'

def true_random_assign_pairs(arr):
    print([arr.pop(random.randrange(len(arr))) for _ in range(2)])
    if len(arr) > 1:
        random_assign(arr)
    else:
        print(arr)

def get_all_pairs(matchee, arr):
    return {matcher: 0 for matcher in arr if matchee != matcher}

def init_pairing_dict(arr):
    return {key: get_all_pairs(key, arr) for key in arr}

def print_and_update_pairs(pairing_dict):
    rem_individuals = list(pairing_dict.keys())
    random.shuffle(rem_individuals)
    rem_individuals = set(rem_individuals)
    while rem_individuals:
        if len(rem_individuals) == 1:
            odd_person = rem_individuals.pop()
            print("Odd person and their record: " + odd_person)
            for pair, count in pairing_dict[odd_person].items():
                print("\t", pair, count)
            return
        pers_a = rem_individuals.pop()
        rem_pairs = {key: pairing_dict[pers_a][key] for key in rem_individuals}
        pers_b = min(rem_pairs, key=rem_pairs.get)
        rem_individuals.remove(pers_b)
        pairing_dict[pers_a][pers_b] += 1
        pairing_dict[pers_b][pers_a] += 1
        print(pers_a + ' - ' + pers_b)

def print_pairing_dict(pdict):
    for student, pairs in pdict.items():
        print(student)
        for name, occ in pairs.items():
            print('\t' + name + ': ', occ)

def read_dict(file):
    try: #little ducktyping -- catches both file not found and file empty (incase it was erased)
        with open(db_name, 'r') as f:
            print("updating db...db_name")
            return json.load(f)
    except (FileNotFoundError, ValueError):
        print("creating db...")
        return init_pairing_dict(student_arr)

def write_dict(file, data):
    with open(db_name, 'w+') as f:
        json.dump(data, f)

def run_test(db_name, student_arr):
    pairing_dict = read_dict(db_name)
    for _ in range(1000):
        print_and_update_pairs(pairing_dict)
    print_pairing_dict(pairing_dict)

def main(db_name, student_arr):
    if sys.version_info[0] < 3:
        print("You are not running this with Python3, --> you will probably need to change range() to xrange()\nTo run with python3, use 'python3' instead of 'python', or alias 'python' to 'python3'")
    pairing_dict = read_dict(db_name)
    print_and_update_pairs(pairing_dict)
    write_dict(db_name, pairing_dict)

main(db_name, student_arr)
# run_test(db_name, student_arr)
