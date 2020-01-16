"""
    This is the implementation of Rabin Karp which is O(mn) algorithm.

    Time Complexity: O(mn)
    
    Uses -
        Plagiarism
"""
import pytest


class RabinKarp:
    def strStr(self, haystack: str, needle: str) -> int:
        # Boundary Cases
        if (not haystack and not needle) or not needle:
            return 0
        if not haystack:
            return -1
        # Initializing some variables
        sizeHaystack = len(haystack)
        sizeNeedle = len(needle)
        hash = 0
        running = 0
        result = -1
        prime = 3

        # Getting Hash function for needle
        if not hash:
            hash = self.getHash(needle, prime)

        # Get Hash function for haystack
        if not running:
            running = self.getHash(haystack[0:sizeNeedle], prime)

        # Loop through haystack to find the match for needle's hash and then compare haystack substring with needle's hash
        for i in range(0, sizeHaystack - sizeNeedle + 1):
            # we check if running hash is same as hash
            if running == hash:
                itr = 0
                found = 1
                for j in range(i, i + sizeNeedle):
                    if haystack[j] == needle[itr]:
                        itr += 1
                    else:
                        found = 0
                        break
                if found:
                    result = i
                    return result
            # if not then we get the hash by removeing prev elem and appending next element
            else:
                running = (running - ord(haystack[i])) // prime
                if (i + sizeNeedle) < sizeHaystack:
                    running += ord(haystack[i + sizeNeedle]) * (
                        prime ** (sizeNeedle - 1)
                    )

        return result

    def getHash(self, str, prime):
        itr = 0
        res = 0
        for j in str:
            res += ord(j) * (prime ** itr)
            itr += 1
        return res


def test_ans():
    tests = [
        ["abcxabcdabxabcdabcdabcy", "abcdabcy", 15],
        ["hello", "ll", 2],
        ["hello", "x", -1],
        ["hello", "", 0],
        ["", "", 0],
        ["", "ll", -1],
        ["l", "ll", -1],
        ["aaaa", "bba", -1],
        ["asd", "", 0],
        [
            "asjkfdhuegfbksjnvjsiadhfiaskjdbfjbeqrigfuisdhvjisodjgokjfsagbkvkxjzgksjdg",
            "jdg",
            70,
        ],
    ]

    rk = RabinKarp()
    for test in tests:
        assert rk.strStr(test[0], test[1]) == test[2]
