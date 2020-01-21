"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other. 

Solution 1: 
    Take a hashmap with key as chars and value as number of occurrences.
    parse through 1st string and count the letters and store in the haspmap
    parse through 2nd string and subtract the count from the hashmap.

    if odd number of characters in the string then only one char should be having 1 count rest 0
    if even number of characters in the string the all the chars will be 0

    Also take a variable which will keep track of the number of unique chars

    Time Complexity  O(n) 
    Space Complexity O(n)
    
"""


class Solution:
    def checkPermutation(s1, s2):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if len(s1) != len(s2):
            return False

        countMap = {}
        uniqueCount = 0

        for char in s1:
            if char in countMap:
                countMap[char] += 1
            else:
                countMap[char] = 1
                uniqueCount += 1
        for char in s2:
            if char in countMap:
                if countMap[char] - 1 == 0:
                    uniqueCount -= 1
                    countMap.pop(char)
                elif countMap[char] - 1 < 0:
                    return False
                else:
                    countMap[char] -= 1
            else:
                return False

        if uniqueCount == 0:
            return True
        else:
            return False
