"""KMK Algorithm - Find the pattern in the string"""


class KMP:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle or (not needle and not haystack):
            return 0
        if not haystack:
            return -1
        prefix = [0] * len(needle)
        j = 0
        for i in range(1, len(needle)):
            while j >= 0:
                if needle[i] == needle[j]:
                    prefix[i] = j + 1
                    j += 1
                    break
                else:
                    if j == 0:
                        prefix[i] == 0
                        break
                    else:
                        j = prefix[j - 1]

        startIndex = -1
        found = 0
        j = 0
        for i in range(len(haystack)):
            while j >= 0:
                if haystack[i] == needle[j]:
                    j += 1
                    if j >= len(needle):
                        found = 1
                        startIndex = i - (j - 1)
                    break
                else:
                    if j == 0:
                        break
                    else:
                        j = prefix[j - 1]
            if found:
                break
        return startIndex


if __name__ == "__main__":
    kmp = KMP()
    arr = [["fjhaoiweyribkcvnkasdfhuoeafiasodjfknlvnkzjflajsohguosahnbf", "asodjf"]]
    for test in arr:
        print(test[0], test[1], kmp.strStr(test[0], test[1]))

