'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

'''
This question is again an example of sliding window problems. and is similar to LeetCode-Problem76

Algorithm:
 - Take 2 pointers x and y both at index 0
 - Move the pointer y in front and push the letter to set and also update the maxSubstring Length until a repeating character is found.
 - This Creates a window from x to y-1.
 - Now once, a repeating character is found, move the pointer x in front.
 - remove the letter from set until the repeating letter is found in the current window with the help of the pointer x.
 - once the letter is found just go to the next index ( which indirectly means removing that letter from current window but adding same letter again which is at index-y to the window.)
 - Now, again repeat from step 2 until the end of string.

 The Time Complexity here is O(n) and not O(n²) because at a time only one pointer is moving. So both the pointer only traverse once. Hence it O(2n) ---> O(n)
'''

class Solution:
    ''' The Time Complexity of this algorithm is O(n) where n is the length of string and the space complexity is O(n) for the set() created. '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        x = 0
        y = 0
        store = 0
        
        if len(s) == 1: 
            return 1
        
        for y in range(len(s)):
            if s[y] not in unique:
                unique.add(s[y])
                store = (y-x+1) if (y-x+1) > store else store
            else:
                found = 0
                while found == 0:
                    if s[x] == s[y]:
                        found = 1
                    else:
                        unique.remove(s[x])
                    x+=1
        return store