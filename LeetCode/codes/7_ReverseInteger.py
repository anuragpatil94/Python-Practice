'''
Given a 32-bit signed integer, reverse digits of an integer.
Example 1:

    Input: 123
    Output: 321
    Example 2:

    Input: -123
    Output: -321
    Example 3:

    Input: 120
    Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x: int) -> int:
        ''' The Time Complexity is  O(log₁₀x) where x is count of digits in the number.'''
        # End Limits
        limitP = 2**31
        limitN = -2**31
        
        # Initiate the Reversed number
        reversed = 0

        # if the number is negative it will be set to 1
        negativeFlag = 0

        if(x > limitP or x < limitN):
            return 0
        
        if x < 0:
            negativeFlag = 1
            x = abs(x)
        
        while x > 0:
            num = x%10
            reversed = (reversed * 10) + num
            x = x//10
        
        if negativeFlag:
            reversed = -reversed
        
        # Check for Limits
        if reversed > limitP or reversed < limitN:
            return 0
        else:
            return reversed
        