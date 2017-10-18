#!/usr/bin/env python
#reducer.py

import string
import sys
import random

# checks the filename list
# for names already added
def check_no_dups(val, lst):
  for item in lst:
    if(item == val):
      return False
  return True

def main():
  first_loop = True
  word_not_printed = True
  current_word = ""
  current_file = ""
  file_list = []

  # for each line in output
  for line in sys.stdin:
    # start of a new line, so
    # reset whether stats have
    # been printed
    word_not_printed = True

    # get words from line
    line = line.rstrip()
    line = line.rstrip('\n')
    words = line.split('\t')

    # set default values on first
    # loop
    if(first_loop):
      current_word = words[0]
      current_file = words[1]
      first_loop = False
      continue

    # if current K,V word and filename
    # are same as previous, skip
    # if word is same, but file is
    # different, then add filename to
    # list of files that have this word
    # in it
    if(words[0] == current_word):
      if(words[1] == current_file):
        continue
      else:
        if(check_no_dups(current_file, file_list)):
          file_list.append(current_file)
    else:
      # if word is different, then add
      # the current filename and print
      # the stats for the previous word
      if(check_no_dups(current_file, file_list)):
        file_list.append(current_file)
      print current_word + "\t" + ",".join(file_list)
      # indicate whether current word
      # stats have been printed
      word_not_printed = False
      # reset file list
      file_list[:] = []

    # always executed, unless continue
    # update current word and filename
    current_word = words[0]
    current_file = words[1]


  # print stats, if last word
  # stats if not already printed
  # this would happen if last
  # K,V pairs received had
  # matching K1s
  # i.e. there,file1.txt  1
  #      there,file2.txt  1
  if(word_not_printed):
    print current_word + "\t" + ",".join(file_list)


main()
