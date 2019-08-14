import unittest
import sys
sys.path.insert(0,"..")

import importlib

class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.target = importlib.import_module("codes.1_TwoSum")
        self.solution = self.target.Solution
        self.twoSum = self.solution.twoSum

    def test_1_Empty(self):
        self.assertEqual(self.twoSum(self.solution, nums = [], target = 9), None, "Should be None. Empty List Passed")

    def test_2_Solution(self):
        self.assertEqual(self.twoSum(self.solution, nums = [2,7,11,15], target = 9), [0,1], "Should be [0,1].")
    
    def test_3_NoSolution(self):
        self.assertEqual(self.twoSum(self.solution, nums = [2,7,11,15], target = 10), None, "Should be None")

if __name__ == "__main__":
    unittest.main()