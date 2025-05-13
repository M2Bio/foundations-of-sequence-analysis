#!/usr/bin/env python3

import re, unittest, string
from editgraph import fillDPtable_minedges
from aligntype import Alignment
from alignment import alignment

def perform_alignment_test(self,u_line,m_line,v_line,with_eop_list=False):
  u = re.sub(r'-','',u_line)
  v = re.sub(r'-','',v_line)
  al = alignment(u,v)
  if with_eop_list:
    print(al.eoplist())
  self.assertEqual(u_line,al.pretty_u_line())
  self.assertEqual(m_line,al.pretty_m_line())
  self.assertEqual(v_line,al.pretty_v_line())

def test_cases_from_file(filename):
  try:
    stream = open(filename)
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  alignment_lines = list()
  for line in stream:
    line = line.rstrip('\n')
    if len(alignment_lines) == 3:
      yield (alignment_lines[0],alignment_lines[1],alignment_lines[2])
      alignment_lines.clear()
    alignment_lines.append(line)
  stream.close()
  assert len(alignment_lines) == 3
  yield (alignment_lines[0],alignment_lines[1],alignment_lines[2])
  
class TestAlignment(unittest.TestCase):
  def test_cases_short(self):
    als = [('CA','||','CA',[('R', 2)]),
           ('CGGCA','|    ','CCTGG',[('R', 5)]),
           ('----ATG-CACCCGA-C-','    ||| |     | | ','AGAAATGTCTGAATATCA',
             [('I',4), ('R',3), ('I',1), ('R',7), ('I',1), ('R',1), ('I',1)]),
           ('CC-A-CCCG--A-T','|| | |  |  | |','CCAAGCATGACAGT',
            [('R',2),('I',1),('R',1),('I',1),('R',4),('I',2),('R',1),
             ('I',1),('R',1)]),
           ('TCTTC--T--TT','| |||  |    ','T-TTCGATGGCC',
            [('R',1),('D',1),('R',3),('I',2),('R',1),('I',2),('R',2)])]
    for u_line, m_line, v_line, al_eoplist in als:
      u = re.sub(r'-','',u_line)
      v = re.sub(r'-','',v_line)
      al = alignment(u,v)
      self.assertEqual(al.eoplist(),al_eoplist)
      perform_alignment_test(self,u_line,m_line,v_line)
  def test_cases_from_file(self):
    for u_line, m_line, v_line in test_cases_from_file('alignments.txt'):
      perform_alignment_test(self,u_line,m_line,v_line)
    
unittest.main()
