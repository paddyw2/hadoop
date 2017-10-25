# if white, do nothing
# if black, do nothing
# if gray, turn black then
# visit all children and turn them gray

# at reducer
import sys

def emit_children_gray(string_adj_list, parent_id, string_distance):
  if(string_adj_list == "NULL"):
    return
  if(string_distance == "Integer.MAX_VALUE"):
    new_distance = string_distance
  else:
    new_distance = int(string_distance) + 1
  adj_list = string_adj_list.split(',')
  for child in adj_list:
    print child + '\t' + "NULL|" + str(new_distance) + "|GRAY|" + parent_id

def main():
  for line in sys.stdin:
    line = line.strip()
    kv_line = line.split('\t')
    line_info = kv_line[1].split('|')
    colour = line_info[2]
    if(colour == "WHITE" or colour == "BLACK"):
      print line
    else:
      line_info[2] = "BLACK"
      # print updated parent
      print kv_line[0] + '\t' + line_info[0] + "|" + \
      line_info[1] + "|" + line_info[2] + "|" + line_info[3]
      # emit all children of parent gray
      emit_children_gray(line_info[0], kv_line[0], line_info[1])


main()
