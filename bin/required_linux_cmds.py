#!/usr/bin/env python3

import sys
from shutil import which

linux_cmds = ['awk',
              'bzip2',
              'cat',
              'cd',
              'cp',
              'chmod',
              'cut',
              'diff',
              'echo',
              'egrep',
              'env',
              'find',
              'grep',
              'gzip',
              'gunzip',
              'head',
              'less',
              'ls',
              'make',
              'man',
              'mkdir',
              'mv',
              'paste',
              'python3',
              'pwd',
              'rmdir',
              'sh',
              'sort',
              'tail',
              'tar',
              'tr',
              'mktemp',
              'touch',
              'wc',
              'xargs',
              'rm']

for cmd in linux_cmds:
  if not which(cmd):
    sys.stderr.write('{}: {} is not in PATH\n'.format(sys.argv[0],cmd))
    exit(1)

print(('{}: all {} required programs are in a directory specified by the '
       'environment variable PATH').format(sys.argv[0],len(linux_cmds)))
