#!/usr/bin/env python3

# main program for affine alignment exercise

import sys, argparse
from fastaIterator import fasta_next
from affinealign import AffineAlignment

def parse_command_line(argv):
  p = argparse.ArgumentParser()
  p.add_argument('-m','--mismatch',type=int,default=1,metavar='<int>',
                 help='specify mismatch cost')
  p.add_argument('-o','--gapopen',type=int,default=3,metavar='<int>',
                 help='specify gap open costs')
  p.add_argument('-e','--gapextend',type=int,default=1,metavar='<int>',
                 help='specify gap extension costs')
  p.add_argument('-c','--onlycost',action='store_true',default=False,
                 help='only output cost of optimal alignment')
  p.add_argument('--show_matrix',action='store_true',default=False,
                 help=('show matrix with (R,D,I)-values for each each matrix '
                       'entry'))
  p.add_argument('inputfiles',nargs='+',
                  help='specify one or two input files')
  args = p.parse_args(argv)
  if len(args.inputfiles) > 2:
    raise argparse.ArgumentTypeError('can only handle one or two input files')
  return args

def all_against_all(args,sequences_list0,sequences_list1):
  for header1, u in sequences_list0:
    for header2, v in sequences_list1:
      if u != v:
        affine_alignment = AffineAlignment(u,v,args.mismatch,
                                           args.gapopen,args.gapextend)
        edist = affine_alignment.affine_edit_distance()
        print('# AffineEdist\t{}\t{}\t{}'.format(header1,header2,edist))
        if not args.onlycost:
          alignment = affine_alignment.optimal_alignment()
          print(alignment)
        if args.show_matrix:
          print(affine_alignment.matrix2string())

try:
  args = parse_command_line(sys.argv[1:])
except argparse.ArgumentTypeError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv,err))
  exit(1)

sequences_lists = list()
for inputfile in args.inputfiles:
  sequences = list()
  for entry in fasta_next(inputfile):
    sequences.append(entry)
  sequences_lists.append(sequences)

if len(sequences_lists) == 1:
  all_against_all(args,sequences_lists[0],sequences_lists[0])
else:
  all_against_all(args,sequences_lists[0],sequences_lists[1])
