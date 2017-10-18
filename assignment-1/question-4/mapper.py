#!/usr/bin/env python
#mapper.py

import string
import sys

def get_hash_identifier(word):
  # 'l' hashes to 0 and
  # is used for numbers
  val = 'l'
  if(word[0].isalpha()):
    val = ord(word[0]) - 97
    # letters are incremented by
    # 12 ascii values to hash to
    # their appropriate values
    val += 12
    # to fit into all reducers
    # modulo by reducer total
    val = val % 27
    val += 97
    val = chr(val)

  return val

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
        id_val = get_hash_identifier(word)
        # print each hash identifier,
        # word, and initial count
        print '%s\t%s\t%s' %(id_val,word,1) 

main()
