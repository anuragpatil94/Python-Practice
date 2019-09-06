'''
URLify: 
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, 
and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.) 

EXAMPLE 
    Input:  "Mr John Smith    ", 13 
    Output: "Mr%20John%20Smith"

Solution 1:
    Since we are given the space to hold additional chars
    traverse from back and start appending the chars

'''

class Solution:
    def URLify(string, size):
        '''
        Time Complexity: O(n)
        Space Complexity: O(1)
        '''
        lenS = len(string)
        for i in range(size-1,-1,-1):
            if(string[i] == " "):
                string[lenS-1] = '0'
                string[lenS-2] = '2'
                string[lenS-3] = '%'
                lenS-=3
            else:
                string[lenS-1] = string[i]
                lenS -=1
        return "".join(string)

if __name__ == "__main__":
    print(Solution.URLify(list("Mr John Smith    "), 13))