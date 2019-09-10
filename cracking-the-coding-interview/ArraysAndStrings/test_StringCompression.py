from CTCI_06_StringCompression import Solution
def test_EmptyString():
    assert Solution().StringCompression("") == ""
def test_OnlySpaceString():
    assert Solution().StringCompression("  ") == " 2"
def test_OneChar():
    assert Solution().StringCompression("A") == "A"
def test_TwoSameChar():
    assert Solution().StringCompression("AA") == "A2"
def test_CompressedLengthGreaterThanActual():
    assert Solution().StringCompression("ABC") == "ABC"
def test_ValidCompression():
    assert Solution().StringCompression("AAABBBCCDEEEEEGGGGGGGTTUU") == "A3B3C2D1E5G7T2U2"
def test_CompressedLengthEqualToActual():
    assert Solution().StringCompression("AABBCCDD") == "A2B2C2D2"