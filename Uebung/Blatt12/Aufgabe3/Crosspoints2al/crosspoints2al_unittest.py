#!/usr/bin/env python3

import sys, re, unittest
from aligntype import Alignment
from crosspoints2al import crosspoints2alignment

def alignment_encoding2alignment(useq,vseq,al_encoding):
  al = Alignment(useq,vseq)
  for mo in re.finditer(r'([RDI])(\d+)',al_encoding):
    eop = mo.group(1)
    nof_ops =  int(mo.group(2))
    if eop == 'R':
      al.add_replacement(nof_ops)
    elif eop == 'D':
      al.add_deletion(nof_ops)
    else:
      assert eop == 'I'
      al.add_insertion(nof_ops)
  return al

def perform_test(self,useq, vseq, distance, crosspoints, al_encoding):
  al_from_cp = crosspoints2alignment(useq,vseq,crosspoints)
  al_from_cp_unitcost = al_from_cp.evaluate()
  self.assertEqual(al_from_cp_unitcost,distance)
  al_from_encoding = alignment_encoding2alignment(useq,vseq,al_encoding)
  self.assertEqual(al_from_encoding,al_from_cp)

class TestCrosspoint2al(unittest.TestCase):
  def test_small(self):
    small_test_data = \
      [('gcact','tgatat',4,[0, 1, 2, 3, 4, 4, 5],'R4I1R1'),
       ('ggactcta','gatatga',4,[0,2,4, 5, 6, 7, 7, 8],'D1R2D1R3I1R1'),
       ('atctcagg','agtatag',4,[0,1,1, 2, 3, 5, 7, 8],'R1I1R3D1R1D1R1')]
    for useq, vseq, distance, crosspoints, al_encoding in small_test_data:
      perform_test(self,useq, vseq, distance, crosspoints, al_encoding)
  def test_large(self):
    try:
      stream = open('large_tests.txt')
    except IOError as err:
      sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
      exit(1)
    for line in stream:
      useq, vseq, distance, crosspoints, al_encoding = eval(line.rstrip())
      perform_test(self,useq, vseq, distance, crosspoints, al_encoding)
    stream.close()

unittest.main()
