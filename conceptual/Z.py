class ZAlgorithm:
    """This algorithm is used for pattern matching. For example, 
       if you want to search if string a exist in string b, 
       This algorithm will perform the operation in O(n+m) time"""

    def __init__(self):
        pass

    def calculateZ(self, string):
        """This method finds the Z array in linear time so that"""
        z = [0] * len(string)
        left, right = 0, 0
        for k in range(1, len(string)):
            if k > right:
                left = right = k
                while right < len(string) and string[right] == string[right - left]:
                    right += 1
                z[k] = right - left
                right -= 1
            else:
                k1 = k - left
                if z[k1] < right - k + 1:
                    z[k] = z[k1]
                else:
                    left = k
                    while right < len(string) and string[right] == string[right - left]:
                        right += 1
                    z[k] = right - left
                    right -= 1
        return z

    def Z(self, pattern, string):
        newString = pattern + "$" + string
        array = self.calculateZ(newString)

        for i in range(len(array)):
            if array[i] == len(pattern):
                return True
        return False


if __name__ == "__main__":
    ZAlgorithm = ZAlgorithm()
    print(ZAlgorithm.Z("ura", "Anurag"))
