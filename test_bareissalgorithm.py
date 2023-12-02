import unittest
from bareissalgorithm import bareissalgorithm

class TestBareissAlgorithm(unittest.TestCase):
    def test_matrix(self):
        matrix = [[ 42, 97, 23 ],[ 51, 30, 77 ],[ 33, 7, 66 ]]
        determinant = bareissalgorithm(matrix)
        self.assertEqual(determinant, -34062, "incorrect determinant")

unittest.main()
