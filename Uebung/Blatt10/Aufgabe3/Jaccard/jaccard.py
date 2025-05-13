#!/usr/bin/env python3

import sys, argparse
from multiseq import Multiseq
from pearson_corr import pearson_correlation
from unique_qgram_list import unique_qgram_list_get, common_get

'''
  Bitte folgende Funktion kurz dokumentieren.
'''

def multiseq2qgram_lists(multiseq,qgram_length):
  return [unique_qgram_list_get(seq_entry.sequence,qgram_length) \
          for seq_entry in multiseq]

'''
  Bitte folgende Funktion kurz dokumentieren.
'''

def all_vs_all(qgram_lists,evaluate):
  n = len(qgram_lists)
  return ((i, j, evaluate(qgram_lists[i],qgram_lists[j])) \
              for i in range(n) for j in range(i+1,n))

'''
  Bitte folgende Funktion kurz dokumentieren.
'''

def common_index(qgram_list1,prefix_length1,qgram_list2,prefix_length2):
  common = common_get(qgram_list1,prefix_length1,qgram_list2,prefix_length2)
  all_unique = prefix_length1 + prefix_length2 - common
  return common/all_unique

'''
  Bitte folgende Funktion kurz dokumentieren.
'''

def all_vs_all_sketch(qgram_lists,sketch_size):
  return all_vs_all(qgram_lists,
                    lambda l1,l2: common_index(l1,min(sketch_size,len(l1)),
                                               l2,min(sketch_size,len(l2))))

'''
  Bitte folgende Funktion kurz dokumentieren.
'''

def all_vs_all_all_qgrams(qgram_lists):
  return all_vs_all(qgram_lists,
                    lambda l1,l2: common_index(l1,len(l1),l2,len(l2)))

def output_result(genresult):
  print('# g1	g2	Jest')
  for r in genresult:
    assert len(r) >= 3
    print('{}\t{}\t{:.5f}'.format(r[0],r[1],r[2]))

def parse_command_line(argv,sketch_size_list):
  default_qgram_length = 16
  p = argparse.ArgumentParser(description='compute jaccard index')
  p.add_argument('-q','--qgram_length',type=int,default=default_qgram_length,
                 metavar='<int>',help=('specify qgram length, default: {}'
                                       .format(default_qgram_length)))
  outputgroup = p.add_mutually_exclusive_group(required=True)
  outputgroup.add_argument('-s','--sketch_size',type=int,default=None,
                           metavar='<int>',
                           help=('compute jaccard index from the smallest s '
                                 'q-grams, where s is the specified sketch '
                                 'size'))
  outputgroup.add_argument('-j','--jaccard',action='store_true',default=False,
                           help='compute jaccard index from all q-grams')
  outputgroup.add_argument('-c','--correlation',action='store_true',
                           default=False,
                           help=('compute correlation of full jaccard index '
                                 'and Jaccard index for sketch size {}')
                                 .format(sketch_size_list))
  p.add_argument('inputfile',type=str,
                  help='specify input file')
  return p.parse_args(argv)

def main():
  sketch_sizes = range(250,1500+1,250)
  args = parse_command_line(sys.argv[1:],list(sketch_sizes))
  multiseq = Multiseq(args.inputfile)
  qgram_lists = multiseq2qgram_lists(multiseq,args.qgram_length)
  jaccard_result = None
  if args.sketch_size:
    sketch_result = all_vs_all_sketch(qgram_lists,args.sketch_size)
    output_result(sketch_result)
  else:
    if args.jaccard or args.correlation:
      jaccard_result = all_vs_all_all_qgrams(qgram_lists);
      if not args.correlation:
        output_result(jaccard_result)
    if args.correlation:
      assert jaccard_result
      jaccard_result_idx_list = [l[2] for l in jaccard_result]
      print('{}\t{}\t{}'.format('# q','s','correlation'))
      for sketch_size in sketch_sizes:
        sketch_result = all_vs_all_sketch(qgram_lists,sketch_size)
        corr = pearson_correlation([l[2] for l in sketch_result],
                                   jaccard_result_idx_list)
        print('{}\t{}\t{:.5f}'.format(args.qgram_length,sketch_size,corr))

if __name__ == '__main__':
  main()
