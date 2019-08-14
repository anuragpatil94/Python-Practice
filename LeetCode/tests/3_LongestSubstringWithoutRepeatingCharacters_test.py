import unittest
import sys
sys.path.insert(0,"..")

import importlib

class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)
        self.target = importlib.import_module("codes.3_LongestSubstringWithoutRepeatingCharacters")
        self.solution = self.target.Solution
        self.lengthOfLongestSubstring = self.solution.lengthOfLongestSubstring

    def test_1_Repeat(self):
        self.assertEqual(self.lengthOfLongestSubstring(self.solution,"abcabcbb"), 3, "Should be 3")

    def test_2_AllSameChar(self):
        self.assertEqual(self.lengthOfLongestSubstring(self.solution,"bbbb"), 1, "Should be 1")
    
    def test_3_End(self):
        self.assertEqual(self.lengthOfLongestSubstring(self.solution,"abcAbca"), 4, "Should be 4")
    
    def test_4_EmptyString(self):
        self.assertEqual(self.lengthOfLongestSubstring(self.solution," "), 1, "Should be 1")
    
    def test_5_AllUnique(self):
        self.assertEqual(self.lengthOfLongestSubstring(self.solution,"abc"), 3, "Should be 1")

if __name__ == "__main__":
    unittest.main()