#!/usr/bin/env python
#mapper.py

import string
import sys

def strip_punc(word):
  for c in string.punctuation:
    word=word.replace(c,"")
  return word

def main():
  # get input from stdin
  for line in sys.stdin:
    # strip whitespace (i.e. "there, was" -> "there,was"
    line = line.strip()
    # move all characters to lowercase
    line = line.lower()
    # split line by comma (default) and generate array
    words = line.split()
    # for each word in the array
    for word in words:
      # for each character in word
      # if it is punctuation, remove it
      word = strip_punc(word)
      if(word != ""):
        val = ord(word[0])-97
        # print each word, with 1 after
        print '%s\t%s' %(word,1) 

main()
