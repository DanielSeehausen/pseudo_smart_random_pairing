## One line install (requires brew)
```bash
bash <(curl -s https://raw.githubusercontent.com/DanielSeehausen/pseudo_smart_random_pairing/master/one_line_install.sh)
```
- checks if you have python3 installed: brew installs it if not
- clones the this repo down
- makes the python script executable
- aliases the script to its installed directory in your ~/.bash_profile (Note: either make one or put the alias in your .profile if you aren't using .bash_profile)
- DO: update the student_arr list in 'smart_assign.py' with the elements you want to randomly pair. Elements must be unique. Syntax is 'student_arr = [el1, el2, el3, etc...]'

### What this does
- enables you to run 'get_pairs' from the command line anywhere (while on the user that installed the script)
- creates a .json file that records pairing results, which the pairing function then uses to make more more evenly distributed pairs in subsequent calls
- reloads your .bash_profile
