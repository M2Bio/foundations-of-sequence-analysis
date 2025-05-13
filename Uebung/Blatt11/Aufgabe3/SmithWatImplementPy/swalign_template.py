from scorematrix import Scorematrix

'''
the following class is used to store the information for the
best entry of the Lmatrix seen so far. It stores the score
value, the row and column number of the best matrix entry
and length values such that there is an alignment of the sequences
u[i-aligned_u...i]
v[j-aligned_v...j]
with the given score. Best means that the score is maximal
and if there is more than one entry with this score, then
the entry which maximizes aligned_u + aligned_v is used. If there
are two entries with maximal score and the same length of the
aligned sequences then the entry which minimizes aligned_v is
chosen.
'''

class BestCoordinate:
  def __init__(self):
    self.score = 0
    self.row = 0
    self.column = 0
    self.aligned_u = 0
    self.aligned_v = 0
  '''
  the following method updates the current best score coordinates and
  the score
  '''
  def update(self,row,column,entry):
    self.score = entry.score
    self.row = row
    self.column = column
    self.aligned_u = entry.aligned_u
    self.aligned_v = entry.aligned_v
  '''
  the following method compares a BestCoordinate entry
  with entry (an instance of class LMatrixEntry) and returns
  True iff entry has a larger score value than maxscore_entry
  or entry has the same score value as maxscore_entry,
  but has longer sum of aligned values than the latter.
  '''
  def better(self,entry):
    # add your code here

'''
the following class stores a value in the L-matrix consisting of a score
and the length aligned_u and aligned_v of the suffixes of u[1...i] and
v[1...j] when computing the entry for (i,j). As an assignmend of a
class instance only copies a reference, we add a copy operation. The string
representation of an LMatrixEntry is a triple with score and the
aligned length on the two sequences.
'''

class LMatrixEntry:
  def __init__(self,score,aligned_u,aligned_v):
    self.score = score
    self.aligned_u = aligned_u
    self.aligned_v = aligned_v
  def copy(self):
    return LMatrixEntry(self.score,self.aligned_u,self.aligned_v)
  def __str__(self):
    return '({},{},{})'.format(self.score,self.aligned_u,self.aligned_v)

'''
This method creates a copy of scol and appends it to the col_list,
which is a list of columns.
'''

def matrix_storecolumn(col_list,scol):
  col_list.append([value.copy() for value in scol])

'''
The following method transposes a matrix, that is, columns and rows
are exchanged. We need it, as we create a list of the columns of the matrix,
but finally need a list of its rows.
'''

def matrix_transpose(matrix):
  columns = len(matrix)
  rows = len(matrix[0])
  t_matrix = [[None] * columns for _ in range(0,rows)]
  for i in range(0,rows):
    for j in range(0,columns):
      t_matrix[i][j] = matrix[j][i]
  return t_matrix

'''
The following method computes the current entry of the
L-matrix in variable curr. we, nw and no are the values
on which it depends (we in the west, nw in the north west
and no in the north). indelscore is the score of an indel
and repscore is the replacement score.
'''

def swcoords_single_entry(indelscore,repscore,curr,we,nw,no):
  # add your code here

'''
this implements the SmithWaterman Algorithm for the given scorematrix,
the indelscore and the sequences useq and vseq. The
L-Matrix is computed column by column and only if
with_matrix is True, the matrix is computed as well. In any case,
the best entry (in the sense as described above) is returned
together with the matrix. This is an empty list for with_matrix = False
and the list of rows of the L-Matrix, otherwise.
'''

def swcoords(scorematrix, indelscore, useq, vseq, with_matrix = False):
  # add comment here: what is initialized and by which values?
  maxscore_entry = BestCoordinate()
  scol = [LMatrixEntry(0,0,0) for _ in range(0,len(useq)+1)]
  matrix = list()
  if with_matrix:
    matrix_storecolumn(matrix,scol)
  for j, cc_b in enumerate(vseq,1):
    # add comment here: what is nw used for?
    # why use copy()?, why use enumerate?
    nw = scol[0].copy()
    for i, cc_a in enumerate(useq,1):
      we = scol[i].copy()
      swcoords_single_entry(indelscore,
                            scorematrix.getscore(cc_a,cc_b),
                            scol[i],
                            we,
                            nw,
                            scol[i-1])
      assert scol[i].score >= 0
      # add comment here: what is the following case distinction
      # used for?
      if maxscore_entry.better(scol[i]):
        maxscore_entry.update(i,j,scol[i])
      nw = we.copy()
    if with_matrix:
      matrix_storecolumn(matrix,scol)
  if with_matrix:
    matrix = matrix_transpose(matrix)
  return maxscore_entry, matrix
