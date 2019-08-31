'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

Solution:
 First check if the character is Alphanumeric
 then either convert to lower case or upper case 
 and check for equality
'''
class Solution:
    ''' Time Complexity is O(n) Space Complexity O(1)'''
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        count = 0
        while j > i:
            if(not s[i].isalnum()):
                i+=1
                continue
            if(not s[j].isalnum()):
                j-=1
                continue
            a = ord(s[i])
            b = ord(s[j])
            
            if(a >= 65 and a <= 90):
                a = a + 32
            if(b >= 65 and b <= 90):
                b = b + 32
            if(a == b):
                i+=1
                j-=1
            if(a!=b):
                return False
        return True