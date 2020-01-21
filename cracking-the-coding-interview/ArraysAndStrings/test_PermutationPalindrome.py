from CTCI_04_PalindromePermutation import Solution


def test_EmptyString():
    assert Solution().PalindromePermutation("") == True


def test_OneChar():
    assert Solution().PalindromePermutation("A") == True


def test_TwoSameChar():
    assert Solution().PalindromePermutation("AA") == True


def test_TwoDifferentChar():
    assert Solution().PalindromePermutation("AB") == False


def test_RandomWord():
    assert Solution().PalindromePermutation("ABCDUTUKW") == False


def test_OddLengthWord():
    assert Solution().PalindromePermutation("ABCDCBA") == True


def test_OddLengthWordInDifferentPos():
    assert Solution().PalindromePermutation("AABBCDC") == True


def test_EvenLengthWord():
    assert Solution().PalindromePermutation("ABCDDCBA") == True


def test_EvenLengthWordInDifferentPos():
    assert Solution().PalindromePermutation("AABBCDDC") == True


def test_AllSameLetters():
    assert Solution().PalindromePermutation("aaaaaaaaaaaaaaaaaaaaaaaaaaa") == True
