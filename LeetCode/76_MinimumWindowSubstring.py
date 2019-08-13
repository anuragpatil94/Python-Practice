import math


class MinimumWindowSubstring:
    def minWindow(self, s: str, t: str) -> str:
        minwindow = tuple((0, math.inf))
        missing = 0
        count = {}
        slow = 0
        fast = 0

        # END TEST CASE
        if(len(s) == 0 or len(t) > len(s)):
            return ""

        # END TEST CASE
        if(s == t):
            return t

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
        assert self.minWindow("","AB") == ""
        assert self.minWindow("A","A") == "A"
        assert self.minWindow("AA","A") == "A"
        assert self.minWindow("AA","AA") == "AA"
        assert self.minWindow("AA","AB") == ""
        assert self.minWindow("ADOBECODEBANC","ABC") == "BANC"
        assert self.minWindow("AJSHIUENAKANHICUAIHU","AHIA") == "AKANHI", "Failed"

        print("ALL TEST CASES PASSED!")


if __name__ == "__main__":
    c = MinimumWindowSubstring()
    c.runTestCases()

