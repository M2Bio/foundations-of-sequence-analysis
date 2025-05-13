#!/usr/bin/env python3

import argparse, sys
import numpy as np

class DistanceMatrix:
  # provide the name of the inputfile with the distance matrix
  def __init__(self,inputfile,mindist=None,eliminate=None):
    try:
      stream = open(inputfile)
    except IOError as err:
      sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
      exit(1)
    self._precision = 5
    self._distance_matrix = None
    self._taxa_names = list()
    self._first = None
    for line_num, line in enumerate(stream,1):
      if line_num == 1:
        try:
          num_of_taxa = int(line.strip())
        except ValueError as err:
          sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
          exit(1)
        self._distance_matrix = np.zeros((num_of_taxa,num_of_taxa))
      else:
        values = line.strip().split()
        possible_lengths = [line_num,line_num-1,num_of_taxa+1]
        if len(values) not in possible_lengths:
          sys.stderr.write(('{}: file {}, line {} does not contain '
                            'exactly {} values\n')
                            .format(sys.argv[0],inputfile,line_num,
                                    ' or '.join(possible_lengths)))
          exit(1)
        taxa_name = values[0].strip()
        self._taxa_names.append(taxa_name)
        for idx, dist_s in enumerate(values[1:]):
          try:
            dist = float(dist_s)
          except ValueError as err:
            sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
            exit(1)
          self._distance_matrix[line_num-2,idx] = dist
          self._distance_matrix[idx,line_num-2] = dist
    if mindist:
      num_of_taxa = len(self._taxa_names)
      close_pairs = [(i,j) for i in range(num_of_taxa) \
                           for j in range(i+1,num_of_taxa)
                           if self._distance_matrix[i,j] < mindist]
      for i,j in close_pairs:
        sys.stderr.write('{}\t{}\n'
                         .format(self._taxa_names[i],self._taxa_names[j]))
    if eliminate:
      dlist = [i for i,taxa_name in enumerate(self._taxa_names) \
                 if taxa_name in eliminate]
      for a in range(0,2):
        self._distance_matrix = np.delete(self._distance_matrix,dlist,axis=a)
      self._taxa_names = [taxa for taxa in self._taxa_names \
                               if not (taxa in eliminate)]

  # return the number of taxa
  def num_of_taxa(self):
    return len(self._taxa_names)
  # return the taxon name for a given taxon index idx
  def taxon_name(self,idx):
    assert idx < self.num_of_taxa()
    return self._taxa_names[idx]
  # return the distance of the two taxa with index i an j
  def distance(self,i,j):
    assert i < self.num_of_taxa() and j < self.num_of_taxa()
    return self._distance_matrix[i,j]
  def set_precision(self,precision):
    self._precision = precision
  def first_set(self,first):
    self._first = first
  def flat_output(self):
    def float2string(f):
      prc = '{:.' + str(self._precision) + 'f}'
      return prc.format(f)
    lines = list()
    num_taxa = len(self._taxa_names)
    if not (self._first is None):
      num_taxa = min(self._first,num_taxa)
    lines.append('# pairwise dist values for {} sequences'.format(num_taxa))
    for idx in range(num_taxa):
      lines.append('{}\t{}'.format(idx,self._taxa_names[idx]))
    for i in range(num_taxa):
      for j in range(i+1,num_taxa):
        lines.append('JKD {} {} {}'
                     .format(i,j,float2string(self._distance_matrix[j][i])))
    return '\n'.join(lines)
  def __str__(self):
    num_taxa = len(self._taxa_names)
    if not (self._first is None):
      num_taxa = min(self._first,num_taxa)
    lines = ['{}{}'.format(num_taxa,'\t' * (num_taxa-1))]
    for i in range(num_taxa):
      this_line = ['{}'.format(self._taxa_names[i])]
      for j in range(num_taxa):
        if j < i:
          prc = '{:.' + str(self._precision) + 'f}'
          this_line.append(prc.format(self._distance_matrix[i,j]))
        elif j > i:
          this_line.append('')
        else:
          this_line.append('0')
      lines.append('\t'.join(this_line))
    return '\n'.join(lines)

def parse_arguments():
  p = argparse.ArgumentParser(description=('read distance matrix'))
  p.add_argument('-p','--precision',type=int,default=5,
                  help='specify precision of floats output (default: 5)')
  p.add_argument('-f','--first',type=int,default=None,
                  help=('specified the number of taxa for which the '
                        'matrix is output'))
  p.add_argument('--flat',action='store_true',default=False,
                 help='show distance values line by line')
  p.add_argument('--mindist',type=float,default=None,
                 help=('specifiy minimum distance value, all taxa which '
                       'have a value smaller than this are eliminated'))
  p.add_argument('-e','--eliminate',nargs='+',
                  help='specify taxa to be eliminated')
  p.add_argument('inputfile',type=str,
                  help='file with distance matrix')
  return p.parse_args()

if __name__ == '__main__':
  args = parse_arguments()
  dm = DistanceMatrix(args.inputfile,args.mindist,args.eliminate)
  if args.first:
    dm.first_set(args.first)
  dm.set_precision(args.precision)
  if args.flat:
    print(dm.flat_output())
  else:
    print(dm)
