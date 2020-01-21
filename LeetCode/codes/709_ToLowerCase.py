"""

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"

idea:
Only Concatenate when found a Capital Letter

"""


class Solution(object):
    def toLowerCase(self, str):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        :type str: str
        :rtype: str
        """
        if str == "":
            return ""

        newString = ""
        strt = 0
        for index, char in enumerate(str, start=0):
            ordChar = ord(char)
            if ordChar >= ord("A") and ordChar <= ord("Z"):
                newString += str[strt:index] + chr(ordChar + 32)
                strt = index + 1
                pass
        return newString + str[strt : index + 1]
