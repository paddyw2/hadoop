# remove duplicates, and update adjacency list
# then emit

# rules: always take the darker score
# always keep darker colour
# always take adj-list from lighter colour

import sys

node_printed = False
first_loop = True
current_node_id = 0
darkest_colour = ""
current_adj_list = []
darkest_score = 0
current_parent = 0

for line in sys.stdin:
  # indicate whether the current node id
  # has been printed to catch if the last
  # 2+ nodes are duplicates
  node_printed = False
  # clean up line
  line = line.strip()
  kv_line = line.split('\t')
  line_info = kv_line[1].split('|')

  # set default values on first loop
  if(first_loop):
    current_node_id = kv_line[0]
    darkest_colour = line_info[2]
    darkest_score = line_info[1]
    current_parent = line_info[3]
    current_adj_list = line_info[0]
    first_loop = False
    continue
  
  # if not first loop, process node
  # if node is duplicate of previous
  # then check for "darker" info
  if(current_node_id == kv_line[0]):
    node_colour = line_info[2]
    # if current node is "darker" than previous nodes, update info
    if(darkest_colour == "WHITE" or \
    (darkest_colour == "GRAY" and node_colour == "BLACK")):
      darkest_colour = node_colour
      darkest_score = line_info[1]
      if(line_info[0] != "NULL"):
        current_adj_list = line_info[0]
      current_parent = line_info[3]
  else:
    # must be a new node, so print previous
    # node condensed stats
    print current_node_id + '\t' + current_adj_list + "|" + \
    darkest_score + "|" + darkest_colour + "|" + current_parent
    node_printed = True
    # now reset info to new node id
    current_node_id = kv_line[0]
    darkest_colour = line_info[2]
    darkest_score = line_info[1]
    current_parent = line_info[3]
    current_adj_list = line_info[0]

# once all lines processed, check to make
# sure last lines were printed
if(False == False):
  print current_node_id + '\t' + current_adj_list + "|" + \
  darkest_score + "|" + darkest_colour + "|" + current_parent
