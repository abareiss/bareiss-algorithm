import unittest
from bareissalgorithm import bareissalgorithm

class TestBareissAlgorithm(unittest.TestCase):
    
    def test_valid_matrix_pos_determinant(self):
        matrix = [[2, 3, 1],[-1, 4, 2],[3, 2, 5]]
        determinant = bareissalgorithm(matrix)
        self.assertEqual(determinant, 51, "incorrect determinant")
        
    def test_valid_matrix_neg_determinant(self):
        matrix = [[ 42, 97, 23 ],[ 51, 30, 77 ],[ 33, 7, 66 ]]
        determinant = bareissalgorithm(matrix)
        self.assertEqual(determinant, -34062, "incorrect determinant")
        
    def test_empty_matrix(self):
        matrix = []
        determinant = bareissalgorithm(matrix)
        self.assertEqual(determinant, 0, "incorrectly determines empty matrix")
        
    def test_zero_matrix(self):
        matrix = [[0,0],[0,0]]
        determinant = bareissalgorithm(matrix)
        self.assertEqual(determinant, 0, "incorrect determinant for zero matrix")

unittest.main()
