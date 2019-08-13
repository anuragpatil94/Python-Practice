import math

'''

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

'''
'''
# pseudocode:
iterate through the string until all the desired characters are in the window.
once all the characters are found store the minwindow and 
iterate the slow pointer until a desired char is removed from the current window.
then again move the fast pointer until the removed char is found again.
        
'''


class MinimumWindowSubstring:
    ''' The Time Complexity for the algorithm is O(s + t) and Space Complexity is O(t) '''

    def minWindow(self, s: str, t: str) -> str:
        # This will store the minimum window everytime missing is set to 0
        minwindow = tuple((0, math.inf))
        # missing will keep track of all the unique characters in the desirable string `t`
        missing = 0
        # count is a dictionary which will keep track of the count of desirable characters in the current window
        count = {}
        # Slow Pointer which will only move once all the desirable characters are in the current window. Start of Window
        slow = 0
        # End Of Window
        fast = 0

        # END TEST CASE - To check if length of t > length of s and also if s is empty string
        if(len(s) == 0 or len(t) > len(s)):
            return ""

        # This will parse through desirable string and count the number of characters and unique characters missing in the string.
        for char in t:
            if(char not in count):
                count[char] = 1
                missing += 1
            else:
                count[char] += 1

        while fast < len(s):
            if s[fast] in count:
                if(count[s[fast]]-1 == 0):
                    missing -= 1
                count[s[fast]] -= 1
            while missing == 0:
                if (fast-slow) < (minwindow[1] - minwindow[0]):
                    minwindow = tuple((slow, fast))
                if(s[slow] in count):
                    count[s[slow]] += 1
                    if (count[s[slow]] > 0):
                        missing += 1
                slow += 1
            fast += 1
        return s[minwindow[0]:minwindow[1]+1] if(minwindow[1] != math.inf) else ""

    def runTestCases(self):
        assert self.minWindow("", "AB") == ""
        assert self.minWindow("A", "A") == "A"
        assert self.minWindow("AA", "A") == "A"
        assert self.minWindow("AA", "AA") == "AA"
        assert self.minWindow("AA", "AB") == ""
        assert self.minWindow("ADOBECODEBANC", "ABC") == "BANC"
        assert self.minWindow("AJSHIUENAKANHICUAIHU",
                              "AHIA") == "AKANHI", "Failed"

        print("ALL TEST CASES PASSED!")


if __name__ == "__main__":
    c = MinimumWindowSubstring()
    c.runTestCases()
