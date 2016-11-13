class Matrix():
    def __init__(self, data):
        self.data = data
        self.det = self.determinant(data)

    def determinant(self, matrix):
        number_of_rows_columns = len(matrix)
        if number_of_rows_columns == 1: # if matrix size is 1x1 return this one element
            return matrix[0][0]

        elif (number_of_rows_columns > 2):
            value = 1
            t = 0
            det = 0
            while t <= number_of_rows_columns - 1: # goes through rows
                d = {}
                row = 1
                while row <= number_of_rows_columns - 1: # goes trough all rows except first,
                    column = 0                           #  to find cofactors for first row
                    d[row]=[]
                    while column <= number_of_rows_columns - 1: # determine 2x2 matrix to find cofactor
                        if (column != t):
                            d[row].append(matrix[row][column])
                        column += 1
                    row += 1
                cofactor = [d[element] for element in d]
                det = det + value * (matrix[0][t]) * (self.determinant(cofactor))   # sum of cofactors
                value = value*(-1)
                t += 1
            return det

        else:
            return (matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])
