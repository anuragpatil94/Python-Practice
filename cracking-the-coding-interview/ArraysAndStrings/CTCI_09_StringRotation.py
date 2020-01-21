"""
String Rotation: 
    Assume you have a method isSubstring which checks if one word is a substring of another. 
    Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat"). 

    My Solution:
        Time Complexity O(n)
        Space Complexity O(1)

        See the point where the 2 string actually start and then check if s1 == yx. if s1 = xy

    Book Solution
        Time Complexity O(n)
        Space Complexity O(1)

        let s1 = xy 
        and s2 be the rotation string  which if it is rotation then it is definitely = yx

        so if we have string s1s1 = xyxy
        hence s2 will always be a subset of s1s1 if s2 is rotation of s1.  ---> yx subset of x yx y

        Since the isSubset() is O(A+B) and Checking for the point of start is O(n) the overall complexity is O(n)        
"""


class Solution:
    def StringRotation(self, s1, s2):
        """
        This will not work for all the cases 
        """
        i = j = 0
        stringIndex = None
        while i < len(s1):
            if s1[i] == s2[j % len(s2)]:
                if not stringIndex:
                    stringIndex = j % len(s2)
                i += 1
                j += 1
            else:
                stringIndex = None
                i = 0
                j += 1
        return True if (s2[stringIndex:] + s2[:stringIndex] == s1) else False


if __name__ == "__main__":
    print(Solution().StringRotation("waterbottle", "erbottlewat"))
    print(
        Solution().StringRotation(
            "abababbbaaabababababaabaabbab", "abababababaabaabbababababbbaa"
        )
    )
