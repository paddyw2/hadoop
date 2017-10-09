#!/usr/bin/env python
#mapper.py

import string
import sys
import os

def strip_punc(word):
  for c in string.punctuation:
    word=word.replace(c,"")
  return word

def main():
  filename = os.getenv('map_input_file')
  filename = filename.split('/')
  filename = filename[len(filename)-1]
  # get input from stdin
  for line in sys.stdin:
    # strip whitespace (i.e. "there, was" -> "there,was"
    line = line.strip()
    # move all characters to lowercase
    line = line.lower()
    # split line generate array
    words = line.split()
    # for each word in the array
    # emit word and its the file
    # it was found in
    #
    for word in words:
      word = strip_punc(word)
      # print each word, with filename after
      print '%s\t%s' %(word,filename)

main()        
