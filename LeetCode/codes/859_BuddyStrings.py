"""
Buddy String
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
 

Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.

Time Complexity = O(n)
Space Complexity = O(1)

"""


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        
        Time: 1 Hour 10 Mins
        """
        if not A or not B:
            return False
        if len(A) != len(B):
            return False
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            pairs = []
            for a, b in zip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) > 2:
                    return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
