"""
This can be solved using greedy method.
The idea is to gothrough each character one by one and compare itsindex with the last occurance of the char in the whole string. 
What this will do it eliminate the fact that if a char is between 0 and 9 and another char is 5 and 15 then, comparing the last occurance will make sure
that the actual division will be between 0 and 15 which will have all the occurances of 2 chars.
"""


class Solution:
    def partitionLabels(self, string):
        arr = []

        last = {}

        i = 0
        while i < len(string):
            last[string[i]] = i
            i += 1

        # short
        # last = {char: idx for idx,char in enumerate(string)}

        start = end = 0
        for i in range(len(string)):
            end = max(end, last[string[i]])
            if end == i:
                arr.append(end - start + 1)
                start = i + 1
        return arr


if __name__ == "__main__":
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))
