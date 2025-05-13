#!/bin/sh

if test $# -ne 1
then
  echo "Usage: $0 <programname>"
  exit 1
fi

program=$1

for m in 0 1 2 3 4 5 6 7 8 9
do
  for n in 0 1 2 3 4 5 6 7 8 9
  do
    ${program} ${m} ${n} | sed -e 's/	(.*//'
  done
done
