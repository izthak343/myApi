import unittest
from functions.myFunctions import multiply,sum 

class TestStringMethods(unittest.TestCase):
    #test the sum and  multiply funsction 
    def test_sum(self):
        self.assertEqual(sum ([1,1,1],[4,5,6]), [5,6,7])

    def test_sum_with_carry(self):
        self.assertEqual(sum ([9,9,9],[1]),[1,0,0,0])
        self.assertEqual(sum ([9,9],[1,1]),[1,1,0])

    def test_sum_with_zero(self):
        self.assertEqual(sum ([9,9,9],[0]),[9,9,9])
        self.assertEqual(sum ([0],[1,1]),[1,1])
        self.assertEqual(sum ([0],[0]),[0])

    def test_sum_with_big_number(self):
        self.assertEqual(sum([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]),[2,4,6,9,1,3,5,7,8])


    def test_multiply(self):
        self.assertEqual(multiply([1,1],[1,1]), [1,2,1])
        self.assertEqual(multiply ([9,9,9],[9,9,9]), [9,9,8,0,0,1])

    def test_multiply_with_zero(self):
        self.assertEqual(multiply ([9,9,9],[0]),[0])
        self.assertEqual(multiply ([0],[1,1]),[0])
        self.assertEqual(multiply ([0],[0]),[0])

    def test_multiply_with_big_number(self):
        self.assertEqual(multiply([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]),[1,5,2,4,1,5,7,8,7,5,0,1,9,0,5,2,1])

if __name__ == '__main__':
    unittest.main()