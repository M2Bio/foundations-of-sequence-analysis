#!/usr/bin/env python3

import unittest
from multiseq import Multiseq
from jaccard import multiseq2qgram_lists, common_index
from unique_qgram_list import unique_qgram_list_get

def jaccard_rows_as_lists(): # value for sequence pairs with q = 16
  input_values = '''0	1	0.65674
0	1	0.65674
0	2	0.69965
0	3	0.00210
0	4	0.58267
0	5	0.58059
1	2	0.74398
1	3	0.00170
1	4	0.52223
1	5	0.51872
2	3	0.00188
2	4	0.55138
2	5	0.55008
3	4	0.00202
3	5	0.00146
4	5	0.98197'''
  for line in input_values.split('\n'):
    yield line.rstrip().split('\t')

def jaccard_sample_rows_as_lists(): # value for sequence pairs with q=16, s=1000
  input_values = '''0	1	0.63666
0	2	0.68492
0	3	0.00100
0	4	0.57356
0	5	0.55521
1	2	0.74064
1	3	0.00050
1	4	0.51515
1	5	0.50150
2	3	0.00050
2	4	0.53374
2	5	0.52555
3	4	0.00100
3	5	0.00100
4	5	0.95503'''
  for line in input_values.split('\n'):
    yield line.rstrip().split('\t')

def compare_with_reference(self,row_list_enum,qgram_lists,s = None):
  for row_list in row_list_enum:
    ci_reference = float(row_list[2])
    i = int(row_list[0])
    len_i = min(s,len(qgram_lists[i])) if s else len(qgram_lists[i])
    j = int(row_list[1])
    len_j = min(s,len(qgram_lists[j])) if s else len(qgram_lists[j])
    ci = common_index(qgram_lists[i],len_i,qgram_lists[j],len_j)
    self.assertLessEqual(abs(ci - ci_reference),1.0e-5)

class TestJaccard(unittest.TestCase):
  def test_jaccard(self):
    qgram_length = 16
    sketch_size = 1000
    multiseq = Multiseq('ebola-genomes.fna')
    qgram_lists = multiseq2qgram_lists(multiseq,qgram_length)
    compare_with_reference(self,jaccard_rows_as_lists(),qgram_lists)
    compare_with_reference(self,jaccard_sample_rows_as_lists(),
                           qgram_lists,sketch_size)

unittest.main()
