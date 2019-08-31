'''

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

'''

class Solution:
    '''Time Complexity: O(n + m) Space Complexity:(n + m)'''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        len1 = len(nums1)
        len2 = len(nums2)
        arr = list()
        i,j = 0,0
        while i < len1 and j < len2:
            if(nums1[i] < nums2[j]):
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        if(i < len1):
            while i < len1:
                arr.append(nums1[i])
                i+=1
        else:
            while j  < len2:
                arr.append(nums2[j])
                j+=1
        
        lenArr = len(arr)
    
        return ((arr[(lenArr//2)-1] + arr[lenArr//2])/2) if lenArr%2==0 else arr[(lenArr//2)]