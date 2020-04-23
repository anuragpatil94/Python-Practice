# class TrieNode:
#     def __init__(self, data={}, stop=False):
#         self.data = data
#         self.stop = stop


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, string):
#         current = self.root
#         currentData = current.data
#         for letter in string:
#             if letter not in currentData:
#                 currentData[letter] = TrieNode()
#             print(letter, currentData.keys())
#             current = currentData[letter]
#             currentData = current.data
#             print(letter, currentData.keys())
#         current.stop = True
#         return

#     def partialSearch(self, string):
#         current = self.root
#         currentData = current.data
#         arr = []
#         string = ""
#         for letter in string:
#             if letter in currentData:
#                 string += letter
#                 # if current.stop:
#                 #     arr.append(string)
#                 current = currentData[letter]
#                 currentData = current.data
#         if current.stop:
#             arr.append(string)
#         if not currentData:
#             return arr
#         for letter in currentData:
#             self.recur(string, current, letter, arr)

#         return arr

#     def recur(self, string, node, letter, arr):
#         current = node
#         currentData = current.data
#         if not currentData:
#             if current.stop:
#                 arr.append(string)
#             return
#         for letter in currentData:
#             string += letter
#             self.recur(string, current, letter, arr)
#         return
#         pass

import bisect


class Solution:
    def suggestedProducts(self, products, searchWord):
        """My Solution - O(s*p + p log p) """
        # Time - p log p
        products.sort()

        # trie = Trie()
        # for product in products:
        #     trie.insert(product)

        arr = []
        search = ""
        # Time O(s)
        for letter in searchWord:
            new = []
            count = 0
            search += letter
            # Time O(p)
            for product in products:
                if product.startswith(search) and count < 3:
                    new.append(product)
                    count += 1
            arr.append(new)
        return arr

    # PYTHON bisect is binary search

    def suggestedProducts2(self, products, searchWord):
        # TOTAL O(s log p + p log p)
        # O(p log p)
        products = sorted(products)
        arr = []
        search = ""
        # O(s)
        for letter in searchWord:
            new = []
            search += letter
            
            # O(log p)
            low = 0
            high = len(products)
            while low < high:
                mid = (low+high)//2
                if products[mid] < search:
                    low = mid+1
                else:
                    high = mid

            # O(s)
            for product in products[low:low+3]:
                if product.startswith(search):
                    new.append(product)
            arr.append(new)
        return arr


if __name__ == "__main__":
    s = Solution()
    print(s.suggestedProducts(["bags", "baggage", "banner", "box", "cloths"], "clothes"))
    print(s.suggestedProducts2(["bags", "baggage", "banner", "box", "cloths"], "clothes"))
