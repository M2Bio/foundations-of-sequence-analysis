#!/usr/bin/env python3

from lcslength import lcslength
import sys, argparse

def parse_command_line(argv):
  p = argparse.ArgumentParser()
  inputgroup = p.add_mutually_exclusive_group(required=True)
  inputgroup.add_argument('--sequences',metavar='<u> <v>',nargs='+',
                          default=None,
                          help='specify pair of sequences')
  inputgroup.add_argument('--filename',metavar='<filename>',type=str,
                          default=None,
                          help='specify filename with reference results')
  args = p.parse_args(argv)
  if args.sequences and len(args.sequences) != 2:
    raise argparse.ArgumentTypeError (('{}: option --sequences requires exactly '
                                       'two arguments').format(sys.argv[0]))
  return args

try:
  args = parse_command_line(sys.argv[1:])
except argparse.ArgumentTypeError as err:
  sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
  exit(1)

if args.sequences:
  useq = args.sequences[0]
  vseq = args.sequences[1]
  print('{}\t{}\t{}'.format(useq,vseq,lcslength(useq,vseq)))
else:
  try:
    stream = open(args.filename)
  except IOError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  linenum = 0
  for line in stream:
    if line.startswith('#'):
      continue
    line = line.rstrip()
    values = line.split('\t')
    useq = values[0]
    vseq = values[1]
    your_lcslength = lcslength(useq,vseq)
    reference_lcslength = int(values[2])
    if your_lcslength != reference_lcslength:
      sys.stderr.write('{}: lcslength({},{})={}\n'
                       .format(sys.argv[0],useq,vseq,reference_lcslength))
      sys.stderr.write('lcs string={}\n'.format(values[3]))
      sys.stderr.write('lcs={}\n'.format(values[4:]))
      sys.stderr.write('but your function delivered the lcslength {}\n'.upper()
                       .format(your_lcslength))
      exit(1)
    linenum+=1
  sys.stderr.write(('{}: computed correct lcslength for {} sequence pairs in '
                    'file {}\n').format(sys.argv[0],linenum,args.filename))
