This directory contains material for the Lcslength exercise

Makefile contains goals test_small and test_large
These trigger the call of lcslength_mn.py for the
input files lcs_testcases_small.tsv and 
lcs_testcases_large.tsv, respectivly. These files contain
sequence pairs, the corresponding lcslength for these
sequence pairs, and lcs-string and a subsequence of maximum
length.

lcslength_mn.py
imports a function lcplength with two arguments and an
integer return value. The latter must be the length of the
longest common subsequence for the two sequence provided
as arguments to the function. It compares the result
delivered by the imported function with the reference result
in the third column of the .tsv inputfile. The additional information
in the remaining columns of the file may be useful for debugging.
