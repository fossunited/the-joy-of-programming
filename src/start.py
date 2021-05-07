"""
start.py
~~~~~~~~

This script is the main entry point. This will be
executed whenever the run button is pressed, after
saving the code in the editor as main.py.

This executes the main.py after adding all the variables
and functions defined in the sketch.py to the executing
environment.
"""

import sketch

# Execute the code in main.py with all the functions
# defined in sketch.py predefined
code = open("main.py").read()
env = dict(sketch.__dict__)
exec(code, env)