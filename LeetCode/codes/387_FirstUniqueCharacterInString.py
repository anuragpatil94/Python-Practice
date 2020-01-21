class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = dict()
        for char in s:
            if char in c:
                c[char] = c[char] + 1
            else:
                c[char] = 1
        for index, char in enumerate(s):
            if c[char] == 1:
                return index
        return -1
