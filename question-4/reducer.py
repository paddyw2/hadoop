#!/usr/bin/env python
#reducer.py

import string
import sys
import random

first_loop = True
current_word = ""
word_count = 0
word_not_printed = True

# for each line in output
for line in sys.stdin:
  # reset print flag
  word_not_printed = True
  # get digram from line
  line = line.rstrip()
  line = line.rstrip('\n')
  words = line.split('\t')

  # set default values on first
  # loop
  if(first_loop):
    current_word = words[0]
    word_count = 1
    first_loop = False
    continue

  # if next word is same as current
  # word, increase word count
  if(words[0] == current_word):
    word_count += 1
  else:
    print current_word + "\t" + str(word_count)
    word_count = 1
    word_not_printed = False

  # always executed, unless continue
  current_word = words[0]

# if last word stats not printed
# due to previous duplicate, print
# them
if(word_not_printed):
  print current_word + "\t" + str(word_count)
