#!/usr/bin/env python3

import random, os.path, sys, importlib
from students import student_arr
from pathlib import Path
from pairs_generator import *
from db_interface import *

db_name = os.path.dirname(os.path.realpath(__file__)) + '/pairing_db.json'

def init_pairing_dict(arr):
    return {key: get_all_pairs(key, arr) for key in arr}

def print_han_solo(han_solo, pairing_dict):
    print("Odd person and their record: " + han_solo)
    for pair, count in pairing_dict[han_solo].items():
        print("\t", pair, count)

def print_pair(rem_individuals, pairing_dict):
    pers_a = rem_individuals.pop()
    rem_pairs = {key: pairing_dict[pers_a][key] for key in rem_individuals}
    pers_b = min(rem_pairs, key=rem_pairs.get)
    rem_individuals.remove(pers_b)
    pairing_dict[pers_a][pers_b] += 1
    pairing_dict[pers_b][pers_a] += 1
    print(pers_a + ' - ' + pers_b)

def print_and_update_pairs(pairing_dict):
    rem_individuals = list(pairing_dict.keys())
    random.shuffle(rem_individuals)
    rem_individuals = set(rem_individuals)
    while rem_individuals:
        if len(rem_individuals) == 1:
            print_han_solo(rem_individuals.pop(), pairing_dict)
        else:
            print_pair(rem_individuals, pairing_dict)

def main(db_name, student_arr):
    print(db_name)
    if sys.version_info[0] < 3:
        print("You are not running this with Python3, --> you will probably need to change range() to xrange()\nTo run with python3, use 'python3' instead of 'python', or alias 'python' to 'python3'")
    pairing_dict = read_dict(db_name)
    print_and_update_pairs(pairing_dict)
    write_dict(db_name, pairing_dict)

main(db_name, student_arr)

# from test import *
# run_test(db_name, student_arr)
