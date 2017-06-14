# What this does
- Somewhat intelligently assigns pairs from an array
- Uses past pair history to inform future pair assignment (does not randomly generate pairs)
- Does not perfectly cycle pairs (i.e. where each element is paired with all others once before seeing a repeat)


## One line install (requires brew)
```bash
bash <(curl -s https://raw.githubusercontent.com/DanielSeehausen/pseudo_smart_random_pairing/master/one_line_install.sh)
```
- you only need to: update the student_arr list in 'smart_assign.py' with the elements you want to randomly pair. Elements must be unique. Syntax is 'student_arr = [el1, el2, el3, etc...]'
- the script:
  - checks if you have python3 installed: brew installs it if not
  - clones the repo down from github
  - makes the python script executable
  - aliases the script to its installed directory in your ~/.bash_profile (Note: either make one or put the alias in your .profile if you aren't using .bash_profile)
  - hax most of your $ecret files

### What this does
- enables you to run 'get_pairs' from the command line anywhere (while on the user that installed the script)
- creates a .json file that records pairing results, which the pairing function then uses to make more more evenly distributed pairs in subsequent calls
- reloads your .bash_profile

### Tidbits
- To reset the db: delete the pairing_db.json file that auto generates after the first time get_pairs is run
- To run a true (or as truly as a computer does) random pairing, use the true_random_assign_pairs function
- to have multiple groups at once:
  - clone to a different directory
  - delete the old db
  - change the array
  - chmod +x smart_assign.py
  - alias it with different name in your .bash_profile
  - source ~/.bash_profile

###### bugs/gripes: daniel.seehausen@gmail.com
