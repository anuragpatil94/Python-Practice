from CTCI_03_URLify import Solution
def test_EmptyString():
    assert Solution.URLify(list(""),0) == ""

def test_String():
    assert Solution.URLify(list("Mr John Smith    "), 13) == "Mr%20John%20Smith"

def test_NoSpace():
    assert Solution.URLify(list("MrSmith"),7) == "MrSmith"

def test_Space():
    assert Solution.URLify(list("   "),1) == "%20"

def test_OneChar():
    assert Solution.URLify(list(" A  "),2) == "%20A"

def test_SpacesBetweenChar():
    assert Solution.URLify(list("A        B                "),10) == "A%20%20%20%20%20%20%20%20B"
