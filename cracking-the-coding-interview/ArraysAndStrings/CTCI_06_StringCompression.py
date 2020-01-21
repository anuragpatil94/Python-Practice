"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters. 

For example, 
    the string aabcccccaaa would become a2blc5a3. 
    If the "compressed" string would not become smaller than the original string, 
    your method should return the original string. 
    You can assume the string has only uppercase and lowercase letters (a -z). 

Solution 1:
    convert string to char array
    start from last char and decrement 
    take 2 pointers - one will decrement and other will keep track of the new compressed string 
        which will be updated in the same string from end.
    everytime a new char is found update the compressed string. 


    Time Complexity : O(n)
    Space Complexity: O(1)

    But this solution will not work when we have to return the original string.
    Hence instead create new string.

    Final Complexity
        Time Complexity : O(n)
        Space Complexity: O(n)

Test Cases

def test_EmptyString()
def test_OneChar()
def test_TwoSameChar()
def test_CompressedLengthGreaterThanActual()
def test_ValidCompression()
def test_CompressedLengthEqualToActual()
"""


class Solution:
    def StringCompression(self, string):
        if not len(string):
            return string

        # To store compressed string
        compressed = ""
        # Iterator for Number of letters in string
        i = 0
        # count of current letters
        count = 0
        current = None
        while i < len(string):
            if not current:
                current = string[i]
            if string[i] is current:
                count += 1
                i += 1
            else:
                current = string[i]
                compressed = "".join([compressed, string[i - 1], str(count)])
                count = 0
            if len(compressed) > len(string):
                return string
        compressed = "".join([compressed, string[i - 1], str(count)])
        if len(compressed) > len(string):
            return string
        return compressed


if __name__ == "__main__":
    s = Solution()
    print(s.StringCompression("AAABBBCCDEEEEEGGGGGGGTTUU"))
