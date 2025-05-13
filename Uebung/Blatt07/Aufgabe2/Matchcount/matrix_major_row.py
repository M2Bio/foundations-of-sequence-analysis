# function to transpose a matrix

def matrix_transpose(matrix,n_rows,n_columns):
  return [[matrix[j][i] for j in range(n_columns)] for i in range(n_rows)]

# function to show a matrix, represented by a list of rows.

def matrix_show(matrix,n_rows,n_columns):
  for i in range(n_rows):
    print([matrix[i][j] for j in range(n_columns)])
