class Solution:
    def reorderLogFiles(self, logs):
        # i = 0
        # j = 0
        # l = len(logs)
        # THIS CAN BE USED SOMEWHERE ELSE
        # while i < l and j < l:
        #     print(logs, i, j)
        #     # Find the Numeric Log
        #     while i < l:
        #         compareElement = logs[i].split(" ")[1]
        #         print(compareElement)
        #         if compareElement.isnumeric():
        #             break
        #         i += 1
        #     j = j + 1
        #     # Find Alphabet and Swap with Numeric
        #     while j < l:
        #         if logs[j].split(" ")[1].isalpha():
        #             logs[i], logs[j] = logs[j], logs[i]
        #             i += 1
        #             break
        #         j += 1

        alpha = []
        num = []
        for log in logs:
            compareElement = log.split(" ")[1]
            if compareElement.isalpha():
                alpha.append((compareElement, log))
            else:
                num.append(log)
        alpha.sort()
        return list(map(lambda x: x[1], alpha)) + num


if __name__ == "__main__":
    s = Solution()
    print(
        s.reorderLogFiles(
            [
                "dig1 8 1 5 1",
                "let1 art can",
                "dig2 3 6",
                "let2 own kit dig",
                "let3 art zero",
            ]
        )
    )
