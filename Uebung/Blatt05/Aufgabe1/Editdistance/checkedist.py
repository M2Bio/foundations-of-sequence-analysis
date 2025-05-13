#!/usr/bin/env python3
# tests the tool calculating the edit distances of short sequences

import sys, re, os, argparse, shlex, subprocess

def parse_command_line(argv):
  p = argparse.ArgumentParser(description='apply tool to test cases')
  p.add_argument('path',type=str,
                  help='specify path of tool to test')
  p.add_argument('testcases',type=str,
                  help=('specify file with testcases in format u\tv\tE '
                        'where u and v are the sequences and E is the unit '
                        'edit distance'))
  return p.parse_args(argv)

args = parse_command_line(sys.argv[1:])

for path in [args.path,args.testcases]:
  if not os.path.isfile(path):
    sys.stderr.write('{}: file "{}" does not exist\n'
                      .format(sys.argv[0],path))
    exit(1)

if not os.access(args.path,os.X_OK):
  sys.stderr.write('{}: file "{}" is not executable\n'
                    .format(sys.argv[0],args.path))
  exit(1)

def enumerate_testcases(filename):
  try:
    stream = open(filename)
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  for line in stream:
    line = line.rstrip()
    mo = re.search(r'^(\w+)\t(\w+)\t(\d+)$',line)
    if mo:
      try:
        edist_expected = int(mo.group(3))
      except ValueError as err:
        sys.stderr.write('{}: {} cannot be parsed as a number\n'
                         .format(sys.argv[0],err))
        exit(1)
      useq = mo.group(1)
      vseq = mo.group(2)
      yield useq, vseq, edist_expected
  stream.close

for useq, vseq, edist_expected in enumerate_testcases(args.testcases):
  cmd_line = '{} {} {}'.format(args.path,useq,vseq)
  cmd_args = shlex.split(cmd_line)
  thispipe = subprocess.Popen(cmd_args,
                              stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE)
  out, _ = thispipe.communicate()
  out_decoded = out.decode().rstrip()
  values = out_decoded.split('\t')
  if len(values) != 3:
    sys.stderr.write('{}: could not parse program output:\n{}\n'
                      .format(sys.argv[0],out_decoded))
    exit(1)
  try:
    edist_result = int(values[2])
  except ValueError as err:
    sys.stderr.write('{}: {} cannot be parsed as a number\n'
                     .format(sys.argv[0],err))
    exit(1)
  if edist_expected != edist_result:
    sys.stderr.write(('Edist({},{})={} was expected, but your program '
                      'returned {}\n')
                      .format(useq,vseq,edist_expected,edist_result))
    exit(1)
  print('Edist({},{})={} is okay'.format(values[0],values[1],values[2]))
