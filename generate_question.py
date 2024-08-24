#! venv/bin/python3

import sys

from create_exercise import create_exercise

try:
    create_exercise(sys.argv[1], sys.argv[2])

except IndexError:
    print('Please put 2 arguments in the function')
