from CTCI_05_OneAway import Solution

def test_EmptyStrings():
    Solution().OneAway("","")
def test_OneLetterBoth():
    Solution().OneAway("A","A")
def test_OneLetterTwoLetter():
    Solution().OneAway("A","BA")
def test_OneInsert():
    Solution().OneAway("A","AD")
def test_OneRemove():
    Solution().OneAway("afghy","afgh")
def test_OneReplace():
    Solution().OneAway("ayghj","aygfj")
def test_Same():
    Solution().OneAway("akgheadphones","akgheadphones")
def test_MoreThanOneChange():
    Solution().OneAway("HGDJ","HGSFJ")