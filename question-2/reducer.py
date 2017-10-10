#!/usr/bin/env python
#reducer.py
import string
import sys
import random

first_loop = True
previous_word_1 = ""
previous_word_2 = ""
digram_count = 0
words = []

# for each line in output
for line in sys.stdin:
  # get digram from line
  line = line.rstrip()
  line = line.strip('\n')
  words = line.split('\t')
  words = words[0].split(',')

  # set default values on first
  # loop
  if(first_loop):
    previous_word_1 = words[0]
    previous_word_2 = words[1]
    digram_count = 1
    first_loop = False
    continue

  # if the next digram is same as
  # previous, increase count and
  # continue without printing
  if(words[0] == previous_word_1  and
      words[1] == previous_word_2):
    digram_count += 1
    continue
  else:
    # if digram is different then print
    # previous digram, along with count
    print previous_word_1 + "," + previous_word_2 + "\t" + str(digram_count)
    # set current digram as new previous
    # and reset count
    previous_word_1 = words[0]
    previous_word_2 = words[1]
    digram_count = 1

# no need to print end loop values, as if not printed at
# end, then last must be duplicate and we are only printing
# unique digrams
if(digram_count == 1):
  print words[0] + "," + words[1] + "\t" + str(digram_count)

