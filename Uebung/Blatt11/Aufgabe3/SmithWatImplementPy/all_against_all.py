#!/usr/bin/env python3

import sys, re, argparse
from fastaIterator import fasta_next

# provides a generator which takes a sequence
# file of, say n lines, and generates all pairs 
# i, j, useq, vseq
# where 0<=i<n and i+1<=j<n and useq is the sequence of line i and
# vseq is sequence of line j

def all_against_all(sequencefile):
  sequences = list()
  if re.search(r'\.fasta$',sequencefile):
    for _, sequence in fasta_next(sequencefile):
       sequences.append(sequence)
  else:
    try:
      stream = open(sequencefile)
    except IOError as err:
      sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
      exit(1)
    for line in stream:
      sequences.append(line.rstrip())
  for i in range(0,len(sequences)-1):
    useq = sequences[i]
    for j in range(i+1,len(sequences)):
      vseq = sequences[j]
      yield i, j, useq, vseq

def parse_command_line(argv):
  p = argparse.ArgumentParser(description=('output all pairs of sequences '
                                           'in file'))
  p.add_argument('inputfile',type=str,help='specify input file')
  return p.parse_args(argv)

if __name__ == '__main__':
  args = parse_command_line(sys.argv[1:])
  for i, j, useq, vseq in all_against_all(args.inputfile):
    print('\t'.join(map(str,[i,j,useq,vseq])))
