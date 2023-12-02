# input is a n-square matrix represented by list of lists. # returns the determinant of the inputted matrix as a float. 
def bareissalgorithm(matrix: list[list]) -> float: 
    int n = len(matrix) # the matrix dimension

    if n <=0:
        return 0
    
    float sign = 1

    for k in range(n-2):
        if matrix[k][k] == 0:
            for m in range(k+1, n-1):
                if matrix[m][k] != 0:
                    swap(matrix[m], matrix[k])
                    sign = -sign
                    break

            # Since all entries were 0 in column k, the determinant is 0
            if (m == n):
                return 0
            

        for i in range(k+1, n-1):
            for j in range(k+1, dim-1):
                matrix[i][j] = matrix[k][k] * matrix[i][j] - matrix[i][k] * matrix[k][i]
                if k!= 0:
                    matrix[i][j] /= matrix[k-1][k-1]

        return sign*matrix[n-1][n-1]



