#!/usr/bin/env python3

import sys, re, os, argparse
from synopsis_enum import synopsis_enum

def synopsis_occurs(synopsis,pattern):
  for value in synopsis.values():
    if re.search(r'{}'.format(pattern),value,flags=re.I):
      return True
  return False

def synopsis_search_all(pattern,filepath,deutsch):
  sys.stderr.write('search \'{}\' in {}\n'.format(pattern,filepath))
  all_keys = ['class','method','call','endesc','dedesc']
  if deutsch:
    show_keys = all_keys.copy()
    show_keys.pop(3)
  else:
    show_keys = all_keys[0:-1]
  previous_output = False
  for synopsis in synopsis_enum(filepath):
    if synopsis_occurs(synopsis,pattern):
      if previous_output:
        print('\n{}\n'.format('-' * 10))
      for idx, key in enumerate(show_keys):
        indent = '  ' * min(2,idx)
        print('{}{}'.format(indent,synopsis[key]))
      previous_output = True

def parse_arguments():
  this_dir = os.path.dirname(os.path.abspath(__file__))
  synopsis_files = ['{}/../data/synopsis.xml'.format(this_dir),
                    '{}/synopsis.xml'.format(this_dir)]
  synopsis_file = None
  for filename in synopsis_files:
    if os.path.isfile(filename):
      synopsis_file = filename
      break
  p = argparse.ArgumentParser(description=('report matches to a given '
                                           'pattern in XML-file'))
  p.add_argument('-d','--deutsch',action='store_true',default=False,
                 help='output description in german')
  p.add_argument('--xmlfile',type=str,default=synopsis_file,
                 help=('specify input file in XML, default: {}'
                       .format(synopsis_file)))
  p.add_argument('pattern',type=str,
                  help='specify pattern to search in synopsis')
  return p.parse_args()

args = parse_arguments()
synopsis_search_all(args.pattern,args.xmlfile,args.deutsch)
