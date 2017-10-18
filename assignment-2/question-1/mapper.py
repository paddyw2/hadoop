import sys

for line in sys.stdin:
  line = line.strip()
  values = line.split(',')
  row = values[0]
  col = values[1]
  val = values[2]
  print col + "," + row + "," + val

