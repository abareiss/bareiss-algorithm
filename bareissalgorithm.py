# input is a n-square matrix represented by list of lists. # returns the determinant of the inputted matrix as a float. 
def bareissalgorithm(matrix: list[list]) -> float: 
    n = len(matrix) # the matrix dimension

    if n <=0:
        return 0
    
    sign = 1

    for k in range(n-1):
        if matrix[k][k] == 0:
            for m in range(k+1, n):
                if matrix[m][k] != 0:
                    swap(matrix[m], matrix[k])
                    sign = -sign
                    break

            # Since all entries were 0 in column k, the determinant is 0
            if (m == n-1):
                return 0
            

        for i in range(k+1, n):
            for j in range(k+1, n):
                matrix[i][j] = matrix[k][k] * matrix[i][j] - matrix[i][k] * matrix[k][j]
                if k!= 0:
                    matrix[i][j] /= matrix[k-1][k-1]

    return sign*matrix[n-1][n-1]



