# Method
- Uses past pair history to inform future pair assignment (does not randomly generate pairs)

# How to use
- Fill in the array in 'students.py' with student names (make any changes to the class here as well)
- after install (see below) use 'get_pairs' in bash anywhere after installing to get a print out of pairs
TODO
- Provide a second argument (i.e. "get_pairs N") to request groups of N size.


## One line install (requires brew)
Run the following directly in bash. It will install the script in the current directory:
```bash
bash <(curl -s https://raw.githubusercontent.com/DanielSeehausen/pseudo_smart_random_pairing/master/one_line_install.sh)
```
- you only need to: update the list in students.py with the elements you want to pair. Elements must be unique. Syntax is 'student_arr = [el1, el2, el3, etc...]'

### Tidbits
- To reset the db: delete the pairing_db.json file that auto generates after the first time get_pairs is run. When no .json file is detected, a new one will be created.
- If you change the list in students.py after you have already run it (e.g. begun building a record of assigned pairs), you will either need to delete the pairing_db.json file and start with a fresh record or selectively remove/add the changes into the .json file. Instead, it is recommended that you manually make the alterations by either slotting the added student(s) in or removing the former student(s) from the results.
