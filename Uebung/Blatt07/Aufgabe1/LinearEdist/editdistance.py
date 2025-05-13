#!/usr/bin/env python3

import sys, argparse
from matrix_major_row import matrix_show

def edelta_evaluate(edelta,u,v,i,j):
  if i == 0:
    return j
  if j == 0:
    return i
  if u[i-1] == v[j-1]:
    repcost = 0
  else:
    repcost = 1
  return min(edelta[i-1][j-1] + repcost,
             edelta[i-1][j] + 1,
             edelta[i][j-1] + 1)

def fillDPtable(u, v):
  m = len(u)
  n = len(v)
  edelta = [[None] * (n+1) for i in range(m+1)]
  for i in range(m+1):
    for j in range(n+1):
      edelta[i][j] = edelta_evaluate(edelta,u,v,i,j)
  return edelta

'''
I have implemented an option parser. The student are not required to
do this as well.'''

def parse_command_line(argv):
  p = argparse.ArgumentParser(description=('compute edit distance for given '
                                           ' input sequences'))
  p.add_argument('-s','--show_matrix',action='store_true',default=False,
                  help='show distance matrix')
  p.add_argument('inputsequence1',type=str,
                 help='specify first input sequence')
  p.add_argument('inputsequence2',type=str,
                 help='specify second input sequence')
  return p.parse_args(argv)

if __name__ == '__main__':
  args = parse_command_line(sys.argv[1:])
  u = args.inputsequence1
  v = args.inputsequence2
  edelta = fillDPtable(u, v)
  m = len(u)
  n = len(v)
  if args.show_matrix:
    matrix_show(edelta,m+1,n+1)
  e = edelta[m][n]
  print('{}\t{}\t{}'.format(u,v,e))
