class TrieNode:
    def __init__(self, data={}, stop=False):
        self.data = data
        self.stop = stop

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        current = self.root
        last = None
        for letter in string:
            if letter not in current.data:
                current.data[letter] = TrieNode()
            current = current.data[letter]
            last = letter
        current.data[letter].stop = True
    def search(self, string):
        current = self.root
        last = None
        for letter in string:
            if letter not in current.data:
                return False
            current = current.data[letter]
            last = letter
        if current.stop:
            return True
        else:
            return False
        pass

    def startsWith(self, string):
        
        pass


if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    t.insert("Jungle")
    print(t.search("app"))
    print(t.search("apple"))
    print(t.search("appl"))