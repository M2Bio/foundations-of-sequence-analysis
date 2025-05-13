#!/usr/bin/env python3

import sys, argparse

def aligns_rec(m,n):
  # to be implemented
  return

def aligns(m,n):
  # to be implemented
  return

def parse_command_line(argv):
  p = argparse.ArgumentParser(description=('compute number of alignments for '
                                           'given sequence lengths'))
  p.add_argument('-r','--recursive',action='store_true',default=False,
                 help='use recursive function')
  p.add_argument('m',type=int,help='specify m')
  p.add_argument('n',type=int,help='specify n')
  args = p.parse_args(argv)
  return args

def check_value(val,tag,maxvalue):
  if val < 0 or val > maxvalue:
    sys.stderr.write('{}: value of {} must be in the range from 0 to {}\n'
                      .format(sys.argv[0],tag,maxvalue))
    exit(1)

if __name__ == '__main__':
  args = parse_command_line(sys.argv[1:])
  maxvalue = 15 if args.recursive else 100
  check_value(args.m,'m',maxvalue)
  check_value(args.n,'n',maxvalue)

  if args.recursive:
    a_number = aligns_rec(args.m,args.n)
  else:
    a_number = aligns(args.m,args.n)
  print('{}\t{}\t{}'.format(args.m,args.n,a_number))
