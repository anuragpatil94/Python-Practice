class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "$".join(s)
        ls = len(s)
        if ls == 0:
            return ""

        print(s)
        # return
        current = 0
        array = [0] * ls
        max = -1
        maxIndex = s[0]
        while current < ls:
            flag = 0
            print(current)
            left = right = 0
            backIter = 0
            offset = 1
            sets = 0
            count = 1
            while current - offset >= 0 and current + offset < ls:
                if s[current - offset] == s[current + offset]:
                    left = current - offset
                    right = current + offset
                    count += 2
                    offset += 1
                else:
                    break

            array[current] = count
            if array[current] > max:
                max = array[current]
                maxIndex = current
            print(array)

            if count == 1:
                current += 1
                continue
            # if current == 3:
            #     break
            offset = 1
            print(current, offset, left, right)
            # print(type(current), type(s[current - offset]))
            # Find Next Current
            while current - offset >= left and current - offset <= right:
                print(
                    "in",
                    current,
                    offset,
                    array[current - offset] // 2,
                    array[current - offset],
                )
                if (current + offset + array[current - offset] // 2) == right:
                    # print("-")
                    array[current + offset] = array[current - offset]
                    current = current + offset
                    break
                elif current + array[current - offset] < right:
                    array[current + offset] = array[current - offset]
                    offset += 1
                elif current + array[current - offset] > right:
                    array[current + offset] = array[current - offset]
                    current = current + offset
                    break
                elif current + array[current - offset] >= ls:
                    flag = 1
                    break
                else:
                    offset += 1

            if sets:
                current = right + 1
            elif flag:
                break
        print(max, maxIndex)
        ans = ""
        compressed = "".join(s.split("$"))
        #         Test Here

        for i in range(len(array)):
            if max == array[i]:
                x = "".join(s[(i - (max // 2)) : (i + (max // 2) + 1)].split("$"))
                if len(x) > len(ans):
                    ans = x

        print(list(s))
        print(list(map(lambda x: str(x), array)))
        return ans


if __name__ == "__main__":
    s = Solution()
    # s.longestPalindrome("cbbd")
    # print("--")
    # s.longestPalindrome("babad")
    # print(s.longestPalindrome("abb"))
    print(s.longestPalindrome("SQQSYYSQQS"))
    # print("--")
    # s.longestPalindrome("abaxabaxabb")
