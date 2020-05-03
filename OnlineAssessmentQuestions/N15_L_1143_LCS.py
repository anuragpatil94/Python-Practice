import collections
import bisect


class Solution:
    def longestCommonSubsequence1(self, text1, text2):
        """
        Time: O(n2)
        Space: O(n2)
        """
        if not text1 or not text2:
            return 0
        m = len(text1)
        n = len(text2)

        # Initializing a 2D array with 0s
        dp = []
        for i in range(m + 1):
            dp.append([0] * (n + 1))

        # For each char of text1 we loop text2 Time O(n^2)
        for i in range(m):
            for j in range(n):
                """
                To Understand this -
                Consider the example
                a = "aabcde"
                b = "bce"

                Our First Match is at i = 2 and j = 0 -> This will make sure 
                that When we reach i=3 and j=1 which is like the next indexes 
                to check then till this position LCS is 1
                """
                # Check if 2 Chars are same
                if text1[i] == text2[j]:
                    # This means that, we found same char and now we can say
                    # that LCS is atleast 1 + LCS to be found in remaining
                    # Chars.
                    # Hence we store this value in the (i+1,j+1) which
                    # shows that for i < i+1 and j < j+1 we found 1 LCS
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    # If the chars are not same then we have 2 options
                    # either increment text1 or increment text2 and
                    # proceed and find the max LCS in them.
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]

    def longestCommonSubsequence2(self, text1, text2):
        """
        Time: O(nlogn)
        Space: O(n+m)
        """

        # Creating a dictionary with default value as empty list.
        memo = collections.defaultdict(list)

        # setting up chars with indexes at which they occur
        for i, a in enumerate(text1):
            memo[a].append(i)

        # Creating a array such that we get all the occurances of char from text2 in text1 and append to list from back
        tmp = []
        for c in text2:
            tmp += memo[c][::-1]
        print(memo)
        print(tmp)

        # Understanding this is very tricky
        def lis(arr):
            dp = [-1]
            # Here n is the index of occurance of character from text2 in text1
            for n in arr:
                if n > dp[-1]:
                    dp.append(n)
                else:
                    # ? Think ABOUT THIS
                    idx = bisect.bisect_left(dp, n)
                    print(dp, idx, n)
                    dp[idx] = n
                print(dp)
            return len(dp) - 1

        return lis(tmp)


if __name__ == "__main__":
    a = "aabcde"
    b = "aace"
    s = Solution()
    print(s.longestCommonSubsequence1(a, b))
    print(s.longestCommonSubsequence2(a, b))
