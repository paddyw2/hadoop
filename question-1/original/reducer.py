#!/usr/bin/env python
#reducer.py

import string
import sys
import random

line_count = 0
max_value = 10
line_number = random.randrange(0,max_value)

for line in sys.stdin:
  print line
