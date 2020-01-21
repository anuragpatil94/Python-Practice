"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures? 

My Solution With additional data structure
- using set to check if a duplicate character exists
"""


class Solution:
    def isUnique(string):
        """
        - Book Solution
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        vector = 0
        for char in string:
            charInt = ord(char)
            if vector & 1 << charInt > 0:
                return False
            vector |= 1 << charInt
            print(bin(vector))
        return True


if __name__ == "__main__":
    s = Solution
    Solution.isUnique("abce")
