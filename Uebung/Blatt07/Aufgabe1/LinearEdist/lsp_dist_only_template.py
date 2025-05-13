#!/usr/bin/env python3

import sys, argparse
from matrix_major_row import matrix_transpose, matrix_show

def nextEDtabcolumn_inplace_unitcost(col,u,b):
  # add your code here

def linearspace_distance_only_unitcost(u,v,debug=False):
  # add your code here

def parse_command_line(argv):
  p = argparse.ArgumentParser(description=('compute edit distance for given '
                                           ' input sequences'))
  p.add_argument('inputsequence1',type=str,
                 help='specify first input sequence')
  p.add_argument('inputsequence2',type=str,
                 help='specify second input sequence')
  return p.parse_args(argv)

if __name__ == '__main__':
  args = parse_command_line(sys.argv[1:])
  u = args.inputsequence1
  v = args.inputsequence2
  edist = linearspace_distance_only_unitcost(u, v, False)
  print('{}\t{}\t{}'.format(u,v,edist))
