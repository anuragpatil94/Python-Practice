from CTCI_01_IsUnique import Solution


def test_EmptyString():
    string = ""
    assert Solution.isUnique(string) == True, "Has Duplicate Characters"


def test_AllUnique():
    string = "abcdefghijklmnopqrstuvwxyz"
    assert Solution.isUnique(string) == True, "Has Duplicate Characters"


def test_Only1Char():
    string = "a"
    assert Solution.isUnique(string) == True, "Has Duplicate Characters"


def test_Only2Char():
    string = "ab"
    assert Solution.isUnique(string) == True, "Has Duplicate Characters"


def test_Only2SameChar():
    string = "aa"
    assert Solution.isUnique(string) == False


def test_SameChars():
    string = "aabbccdd"
    assert Solution.isUnique(string) == False


def test_SameCharsInTheEnd():
    string = "abcdefff"
    assert Solution.isUnique(string) == False


def test_SameCharInRandomPos():
    string = "agndheyjsmoplqg"
    assert Solution.isUnique(string) == False
