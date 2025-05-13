#!/usr/bin/env python3

import sys, re, argparse
from string_matching import string_matching_fast

def parse_command_line(argv):
  p = argparse.ArgumentParser(description='run fast string match algorithm')
  p.add_argument('textfile',type=str,help='specify textfile')
  p.add_argument('patternfile',type=str,help='specify patternfile')
  return p.parse_args(argv)

args = parse_command_line(sys.argv[1:])

stream_list = list()
for idx in range(0,2):
  try:
    filename = args.textfile if idx == 0 else args.patternfile
    stream = open(filename)
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  stream_list.append(stream)

text = re.sub(r'\s','',stream_list[1].read())
stream_list[1].close
for pattern in stream_list[0]:
  pattern = pattern.rstrip()
  ratio = string_matching_fast(pattern,text)
  print("{}\t{:.0f}%".format(pattern,ratio))
stream_list[0].close
