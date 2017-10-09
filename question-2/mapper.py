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
      # so for there,was,a,string it would emit
      # there,was
      # was,a
      # a,string
      #
      counter = 0
      while counter < len(words)-1:
        word1 = strip_punc(words[counter])
        word2 = strip_punc(words[counter+1])
        # print first word as key to allow the
        # partioner to hash all same digrams to
        # same reducer
        print'%s,%s\t%s' %(word1,word2,1)
        counter += 1

main()        
