#!/usr/bin/env python3

import sys, re
from aligntype import Alignment

def delgaps(s):
  return re.sub(r'-','',s)

def cigar2al(al,cigarstring):
  for m in re.findall(r'([MDI])(\d+)',cigarstring):
    eop = m[0]
    multiplier = None
    try:
      multiplier = int(m[1])
    except ValueError as err:
      sys.stderr.write('{}: cannot parse integer from {}\n'
                        .format(sys.argv[0],err))
      exit(1)
    if eop == 'M':
      al.add_replacement(multiplier)
    elif eop == 'I':
      al.add_insertion(multiplier)
    else:
      assert eop == 'D'
      al.add_deletion(multiplier)

def compare_string(line_num,s,t):
  print(s)
  print(t)
  idx = 0
  while idx < min(len(s),len(t)):
    # print('{} {}'.format(s[idx],t[idx]))
    assert s[idx] == t[idx], \
           ('{}: s[{}] = {} != {} = t[{}]'
            .format(sys.argv[0],idx,s[idx],t[idx],idx))
    idx += 1
  while idx < len(s):
    # print('{} ?'.format(s[idx]))
    assert False, '{}: idx = {} < {}'.format(sys.argv[0],idx,len(s))
    idx += 1
  while idx < len(t):
    # print('? {}'.format(t[idx]))
    assert False, '{}: idx = {} < {}'.format(sys.argv[0],idx,len(t))
    idx += 1

def compare(sl,tl):
  assert len(sl) == len(tl) and len(sl) == 3
  for line_num in range(0,3):
    compare_string(line_num,sl[line_num],tl[line_num])

if len(sys.argv) != 2:
  sys.stderr.write('Usage: {} <filename>\n'.format(sys.argv[0]))
  exit(1)

inputfile = sys.argv[1]
try:
  stream = open(inputfile,'r')
except IOError as err:
  sys.stderr.write('{}: cannot open file {}: {}'
                    .format(sys.argv[0],inputfile,err))
  exit(1)
   
ls = list()
for line_num, line in enumerate(stream):
  line = line.rstrip('\n')
  assert len(ls) < 4
  ls.append(line)
  if len(ls) < 4:
    continue
  assert len(ls) == 4
  dseq = ls[0]
  dlen = len(dseq)
  qseq = ls[2]
  qlen = len(qseq)
  assert dlen == qlen, ('{}: {}, l. {}, dlen={} != {}=qlen,ls={}'
                        .format(sys.argv[0],inputfile,line_num,dlen,qlen,ls))
  alen = len(ls[1])
  if alen < qlen:
    aseq = ls[1] + (' ' * (qlen - alen))
  else:
    aseq = ls[1]
  cigarstring = ls[3]
  al = Alignment(delgaps(dseq),delgaps(qseq))
  cigar2al(al,cigarstring)
  p_formatted = (al.pretty_u_line(),al.pretty_m_line(),al.pretty_v_line())
  o_formatted = (dseq,aseq,qseq)
  if p_formatted != o_formatted:
    sys.stderr.write('p_formatted =\n{}\n!=\n'.format(p_formatted))
    sys.stderr.write('o_formatted =\n{}\n'.format(o_formatted))
    if len(p_formatted) != len(o_formatted):
      sys.stderr.write('len(p_formatted) = {} != {} = len(o_formatted)\n'
                        .format(len(p_formatted),len(o_formatted)))
    compare(p_formatted,o_formatted)
    exit(1)
  ls.clear()
