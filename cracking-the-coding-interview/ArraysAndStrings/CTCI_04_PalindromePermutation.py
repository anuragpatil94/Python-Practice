"""

Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words. 

EXAMPLE 
    Input: Tact Coa 
    Output: True (permutations: "taco cat", "atco cta", etc.) 


Solution 1:
    Take a HashMap and save the char and its counts to it
    if number of letters are odd then one of the character should have odd count

Solution 2:
    

Assuming that the string only contains a-zA-Z
    
"""


class Solution:
    def PalindromePermutation(self, string):
        vector = 0
        if string is None:
            return None
        for char in string:
            if char is None or (" " in char):
                continue
            charInt = self.getOrd(ord(char))
            vector ^= 1 << charInt
        if vector > 0:
            if vector & (vector - 1) == 0:
                return True
            else:
                return False
        else:
            return True

    def getOrd(self, charInt):
        if charInt >= 65 and charInt <= 90:
            return 26 + (charInt - ord("A"))
        else:
            return charInt - ord("a")
