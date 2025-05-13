#!/usr/bin/env python3

import sys, argparse

def massmatches_enum(weight_dict,sequence,weight):
 # add your code here

def parse_command_line(args):
  p = argparse.ArgumentParser(description='Solve massmatching problem')
  inputgroup = p.add_mutually_exclusive_group(required=True)
  inputgroup.add_argument('-f','--filename',type=str,default=None,
                          help=('specify inputfile with DNA sequences and '
                                'mass in white space separated lines'))
  inputgroup.add_argument('-s','--sequence',type=str,
                 help=('specify DNA-sequence with mass in a single white space '
                       'string g, and t'))
  return p.parse_args(args)

def process_sequence_with_weight(s):
  arr = s.split()
  if len(arr) < 2:
    sys.stderr.write('{}: illegal specification \'{}\' of sequence and weight\n'
                        .format(sys.argv[0],s))
    exit(1)
  try:
    weight = int(arr[1])
  except ValueError as err:
    sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
    exit(1)
  return arr[0], weight

def enum_queries(alphabet,args):
  def sequence_is_valid(sequence):
    for cc in sequence:
      if not cc in alphabet:
        sys.stderr.write('{}: found unweighted symbol: {}\n'
                           .format(sys.argv[0],cc))
        exit(1)
  if args.sequence:
    sequence, weight = process_sequence_with_weight(args.sequence)
    sequence_is_valid(sequence)
    yield sequence, weight
  else:
    try:
      stream = open(args.filename)
    except IOError as err:
      sys.stderr.write('{}: {}\n'.format(sys.argv[0],err))
      exit(1)
    for line in stream:
      sequence, weight = process_sequence_with_weight(line.rstrip())
      sequence_is_valid(sequence)
      yield sequence, weight
    stream.close()

def main():
  args = parse_command_line(sys.argv[1:])

  # weight function as dictionary
  weight_dict = {'a' : 1, 'A' : 1,
                 'c' : 2, 'C' : 2,
                 'g' : 3, 'G' : 3,
                 't' : 2, 'T' : 2}
  for sequence, weight in enum_queries(set(weight_dict.keys()),args):
    print('# {}\t{}'.format(sequence,weight))
    for start_pos, length in massmatches_enum(weight_dict,sequence,weight):
      print('{}\t{}'.format(start_pos,length))

main()
