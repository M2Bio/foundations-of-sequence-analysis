#!/usr/bin/env python3

import sys, argparse
from matrix_major_row import matrix_show


def matchcount_matrix(useq, vseq, q):
 # add your code here
 return

def matchcount_bf(s,t):
  mc = 0
  for idx in range(0,len(s)):
    if s[idx] == t[idx]:
      mc += 1
  return mc

def matrix_check(mat,useq,vseq,q):
  m = len(useq)
  n = len(vseq)
  for i in range(m-q+1):
    for j in range(n-q+1):
      u_qgram = useq[i:i+q]
      v_qgram = vseq[j:j+q]
      mc_bf = matchcount_bf(u_qgram,v_qgram)
      mc = mat[i][j]
      if mc != mc_bf:
        sys.stderr.write('{}: mc({},{}) = {} != {} = mc_bf'
                         .format(sys.argv[0],u_qgram,v_qgram,mc,mc_bf))
        exit(1)

def parse_command_line(argv):
  p = argparse.ArgumentParser()
  p.add_argument('useq',metavar='<seq>',type=str,default=None,
                 help='specifiy useq')
  p.add_argument('vseq',metavar='<seq>',type=str,default=None,
                 help='specifiy vseq')
  p.add_argument('-m','--matrix',action='store_true',default=False,
                  help='show matrix')
  p.add_argument('-c','--check',action='store_true',default=False,
                  help='check if values in matrix are correct')
  p.add_argument('q',type=int,default=None,help='specifiy q')
  return p.parse_args(argv)

args = parse_command_line(sys.argv[1:])

useq = args.useq
vseq = args.vseq
q = args.q
m = len(useq)
n = len(vseq)
if m >= q and n >= q:
  total_count_cmp, mat = matchcount_matrix(useq,vseq,q)
  num_of_values = (m-q+1) * (n-q+1)
  print('# comparisons per entry: {:.2f}'
        .format(total_count_cmp/num_of_values))
  if args.matrix:
    matrix_show(mat,m-q+1,n-q+1)
  if args.check:
    matrix_check(mat,useq,vseq,q)
