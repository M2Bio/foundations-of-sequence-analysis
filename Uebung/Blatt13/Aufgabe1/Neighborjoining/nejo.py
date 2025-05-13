#!/usr/bin/env python3

import sys, re, argparse
from dist_matrix import DistanceMatrix
from nejo_class import NeighborJoining

def format_edge(precision,parent,children,d2c):
  prc = '{:.' + str(precision) + 'f}'
  assert len(children) == 2
  if parent:
    assert len(d2c) == 2
    return (('{}\t{}\t{}\t' + prc + '\t' + prc)
            .format(parent,children[0],children[1],d2c[0],d2c[1]))
  assert len(d2c) == 1
  return (('{}\t{}\t' + prc).format(children[0],children[1],d2c[0]))

def parse_arguments():
  p = argparse.ArgumentParser(description=('compute phylogenetic tree using '
                                           'the neighbor joining algorithm'))
  p.add_argument('-p','--precision',type=int,default=5,
                  help='specify precision of floats output (default: 5)')
  p.add_argument('inputfile',type=str,
                  help='file with distance matrix')
  return p.parse_args()

args = parse_arguments()

dm = DistanceMatrix(args.inputfile)
nejo = NeighborJoining(dm)
for parent, children, d2c in nejo.enum_tree_edges():
  print(format_edge(args.precision,parent,children,d2c))
