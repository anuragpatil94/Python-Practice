'''
One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. 
Given two strings, write a function to check if they are one edit (or zero edits) away. 

EXAMPLE 
    pale, ple -> true 
    pales, pale -> true 
    pale, bale -> true 
    pale, bake -> false 

Solution 1:
    take s1 and s2 where s1 is always(if) smaller than s2.
    traverse through s1 (smaller string) and compare it with the s2.
    if a change is occurred - keep a check with a flag.
    if a change occurred again return false else return true if only one change.

    Time Complexity 0(n) where n is the length of the smaller string.

    Test Cases

    def test_EmptyStrings()
    def test_OneLetterBoth()
    def test_OneLetterTwoLetter()
    def test_OneInsert()
    def test_OneRemove()
    def test_OneReplace()
    def test_Same()
    def test_MoreThanOneChange()
'''

class Solution:
    def OneAway(self, s1, s2) -> bool:
        if len(s2) < len(s1):
            s1,s2 = s2,s1
        if len(s2) - len(s1) > 1:
            return False 
        same = 0
        if len(s1) == len(s2):
            same = 1
        index1 = index2 = 0
        change = 0
        for index in range(len(s1)):
            if s1[index1] == s2[index2]:
                index2+=1
                index1+=1
            else:
                if not change:
                    change+=1
                    if same:
                        index1 += 1
                    index2 += 1
                else:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()

    l = [ ["pale", "ple" ],
    ["pales", "pale" ],
    ["pale", "bale"  ],
    ["pale", "bake"]]

    for x in l:
        print(s.OneAway(x[0],x[1]))