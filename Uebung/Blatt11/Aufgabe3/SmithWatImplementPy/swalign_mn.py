#!/usr/bin/env python3

import sys, argparse
from scorematrix import Scorematrix
from all_against_all import all_against_all
from swalign import swcoords, BestCoordinate

def parse_command_line(argv):
  p = argparse.ArgumentParser()
  p.add_argument('-f','--force_order',action='store_true',default=False,
                 help='force original order of the two sequences')
  p.add_argument('-m','--show_matrix',action='store_true',default=False,
                 help='show matrix besides coordinates')
  p.add_argument('-l','--latex',action='store_true',default=False,
                 help='show matrix in latex format')
  p.add_argument('-o','--orig',action='store_true',default=False,
                 help=('show most distance orig rather than length of aligned '
                       ' sequences'))
  p.add_argument('-i','--indelpenalty',type=int,default=4,metavar='<int>',
                 help='specify penalty >= 1 for insertion and deletion')
  p.add_argument('-s','--scorematrix',type=str,default='blosum62.txt',
                 metavar='<filename>',
                 help='specify name of file with score_matrix in Blast format')
  p.add_argument('inputfile',type=str,help='specify input file')
  args = p.parse_args(argv)
  if args.indelpenalty < 1:
    sys.stderr.write('{}: penalty for indel must be positive integer\n'
                      .format(sys.args[0]))
    exit(1)
  return args

def showmatrix(matrix,show_orig,latex = False):
  if latex:
    sep = '&'
    final = '\\\\'
  else:
    sep = '\t'
    final = ''
  if latex:
    print('% created by {}'.format(' '.join(sys.argv)))
    print('% rows={}'.format(len(matrix)))
    print('% columns={}'.format(len(matrix[0])))
    print('\\begin{{tabular}}{{r*{{{}}}{{c}}}}'.format(len(matrix[0])))
    index_line = sep.join(map(str,range(0,len(matrix[0]))))
    print('&{}{}'.format(index_line,final))
  for i in range(0,len(matrix)):
    if latex:
      row = [i]
    else:
      row = list()
    for j in range(0,len(matrix[i])):
      if show_orig:
        val = matrix[i][j]
        assert i >= val.aligned_u
        assert j >= val.aligned_v
        row.append((val.score,i - val.aligned_u,j - val.aligned_v))
      else:
        row.append(matrix[i][j])
    print('{}{}'.format(sep.join(map(str,row)),final))
  if latex:
    print('\\end{tabular}')

args = parse_command_line(sys.argv[1:])

scorematrix = Scorematrix(args.scorematrix)
print(('# Fields: s. seqnum, q. seqnum, s. start, s. len, q. start, '
       'q. len, score'))
for i, j, useq, vseq in all_against_all(args.inputfile):
  result = [i,j]
  matrix = None
  if args.force_order or len(useq) < len(vseq):
    bestcoord, matrix = swcoords(scorematrix,-args.indelpenalty,useq,vseq,
                                 args.show_matrix)
    result.append(bestcoord.row - bestcoord.aligned_u)
    result.append(bestcoord.aligned_u)
    result.append(bestcoord.column - bestcoord.aligned_v)
    result.append(bestcoord.aligned_v)
  else:
    bestcoord, matrix = swcoords(scorematrix,-args.indelpenalty, vseq,useq,
                                     args.show_matrix)
    result.append(bestcoord.column - bestcoord.aligned_v)
    result.append(bestcoord.aligned_v)
    result.append(bestcoord.row - bestcoord.aligned_u)
    result.append(bestcoord.aligned_u)
  if args.show_matrix:
    showmatrix(matrix,args.orig,args.latex)
  result.append(bestcoord.score)
  print('\t'.join(map(str,result)))
