#!/usr/bin/env python3

import sys, argparse

'''
order of bits/boolean values for minedges is D I R

we use a bit representation, i.e. the mask to the D-bit is 1 << 2 = 100 = 4,
the mask to the I-bit is 1 << 1 = 010 = 2 and the mask to the R-bit is
1 = 001. The following function returns a triple with these masks.
It is also used in the traceback method
'''

def seteopbits():
  return 1 << 2, 1 << 1, 1

def fillDPtable_minedges(u, v):
  m = len(u)
  n = len(v)
  dbit, ibit, rbit = seteopbits()
  edelta = [[None] * (n+1) for i in range(m+1)]
  for i in range(m+1):
    for j in range(n+1):
      if i == 0:
        if j == 0:
          minedgeI = False
          edelta[i][j] = (j,0)
        else:
          edelta[i][j] = (j,ibit)
      elif j == 0:
        edelta[i][j] = (i,dbit)
      else:
        fromD = edelta[i-1][j][0] + 1
        fromI = edelta[i][j-1][0] + 1
        if u[i-1] == v[j-1]:
          fromR = edelta[i-1][j-1][0]
        else:
          fromR = edelta[i-1][j-1][0] + 1
        mincost = min(fromD,fromI,fromR)
        minedgebits = 0
        if mincost == fromD:
          minedgebits |= dbit
        if mincost == fromI:
          minedgebits |= ibit
        if mincost == fromR:
          minedgebits |= rbit
        edelta[i][j] = (mincost,minedgebits)
  return edelta

'''
this function gets the bit reprenttion of the incoming minimizing edges
it iterates over the three masks and collects the corresponding characters
signifying whether the bit was set or not. The list ist joined to return
string
'''

def bits_pretty(minedgebits):
  l = list()
  dbit, ibit, rbit = seteopbits()
  for mask in [dbit,ibit,rbit]:
    if minedgebits & mask:
      l.append('1')
    else:
      l.append('0')
  return ''.join(l)

# show the matrix with a distance value and the minedges bits

def showmatrix(edelta,m,n):
  for i in range(m+1):
    ll = list()
    for j in range(n+1):
      bits = bits_pretty(edelta[i][j][1])
      d = edelta[i][j][0]
      ll.append('{}/{}'.format(d,bits))
    print('{}'.format('\t'.join(ll)))

if __name__ == "__main__":
  p = argparse.ArgumentParser()
  p.add_argument("-n","--nomatrix",action='store_true',default=False,
                 help=("do not show edit matrix with distance value and "
                       "minedge bits"))
  p.add_argument("inputsequence1",type=str,
                 help="specify first input sequence")
  p.add_argument("inputsequence2",type=str,
                 help="specify second input sequence")
  args = p.parse_args(argv)
  u = args.inputsequence1
  v = args.inputsequence2
  edelta = fillDPtable_minedges(u, v)
  m = len(u)
  n = len(v)
  d = edelta[m][n][0]
  print('{}\t{}\t{}'.format(u,v,d))
  if not args.nomatrix:
    showmatrix(edelta,m,n)
