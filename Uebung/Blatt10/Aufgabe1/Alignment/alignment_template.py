#!/usr/bin/env python3

import sys, argparse
from editgraph import fillDPtable_minedges, seteopbits
from aligntype import Alignment


def traceback(al,matrix,m,n):
  # to be implemented

def alignment(u,v):
  # to be implemented

def parse_command_line(argv):
  p = argparse.ArgumentParser()
  p.add_argument('-d','--edit_distance',action='store_true',default=False,
                  help='output edit distance')
  p.add_argument('-a','--alignment',action='store_true',default=False,
                  help='output alignment in three lines')
  p.add_argument('-e','--eoplist',action='store_true',default=False,
                  help='output alignment as list of multi edit operations')
  p.add_argument('-f','--files',action='store_true',default=False,
                  help=('interpret positonal arguments as filenames in '
                        'fasta format'))
  p.add_argument('input1',type=str,
                 help='specify first input sequence')
  p.add_argument('input2',type=str,
                 help='specify second input sequence')
  return p.parse_args(argv)

if __name__ == '__main__':
  args = parse_command_line(sys.argv[1:])
  if args.files:
    from fastaIterator import fasta_next
    for _, sequence in fasta_next(args.input1):
      u = sequence
      break
    for _, sequence in fasta_next(args.input2):
      v = sequence
      break
  else:
    u = args.input1
    v = args.input2
  al = alignment(u,v)
  if args.eoplist:
    print(al.eoplist())
  if args.alignment:
    print(al)
  if args.edit_distance:
    print(al.evaluate())
