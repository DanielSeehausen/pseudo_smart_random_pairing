import json

def read_dict(db_name):
    try: #little ducktyping -- catches both file not found and file empty (incase it was erased)
        with open(db_name, 'r') as f:
            print("updating db...db_name")
            return json.load(f)
    except (FileNotFoundError, ValueError):
        print("creating db...")
        return init_pairing_dict(student_arr)

def write_dict(db_name, data):
    with open(db_name, 'w+') as f:
        json.dump(data, f)
