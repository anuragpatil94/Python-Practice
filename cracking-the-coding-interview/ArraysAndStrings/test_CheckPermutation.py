from CTCI_02_CheckPermutation import Solution


def test_EmptyString():
    assert Solution.checkPermutation("", "") == True


def test_OneChar():
    assert Solution.checkPermutation("A", "A") == True


def test_SameCharOdd():
    assert Solution.checkPermutation("AAAAA", "AAAAA") == True


def test_SameCharEven():
    assert Solution.checkPermutation("AAAA", "AAAA") == True


def test_SameCharDifferentCount():
    assert Solution.checkPermutation("AAA", "AAAA") == False


def test_DifferentChars():
    assert Solution.checkPermutation("AbCdE", "ZErio") == False


def test_DifferentCharPerm():
    assert Solution.checkPermutation("AbCdE", "ECAdb") == True
