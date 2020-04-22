"""
AMAZON
Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to least frequently mentioned.

The comparison of strings is case-insensitive. If keywords are mentioned an equal number of times in reviews, sort alphabetically.

Example 1:

Input:
k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]

Output:
["anacell", "betacellular"]

Explanation:
"anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.
Example 2:

Input:
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

Output:
["betacellular", "anacell"]

Explanation:
"betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews, but "anacell" is lexicographically smaller.
"""
import heapq
import re


class Solution:
    def TopK(self, keywords, reviews, k):
        '''
        Time Complexity - O(N + (k log k)) - Where N is number of words in the reviews and k is number of keywords. 
        Once all the words are processed in O(N) times the only words remaining are number of keywords. 
        So all Other Processing will be done on 'k' words.
        
        '''

        # Set of Keywords which are used as a dictionary to only consider these words while creating count. 
        # Space - O(k)
        keys = set(keywords)
        # Dictionary of count of words(keywords) in each reviews. Word Count Max=1 for each review.
        # If a review contains a word more than once it will be considered only once 
        # Space - O(k)
        count = {}
        # Time - O(N)
        for review in reviews:
            words = review.lower().split()
            # This will be set of words alredy counted for each review. This is used to minimize the count of word only once per review. 
            # Space O(k)
            uniqueToReviews = set()
            for word in words:
                word = re.sub("[^a-z]", "", word)
                # This makes sure the word is subset of keywords and is not considered before in the review.
                if word in keys and word not in uniqueToReviews:
                    uniqueToReviews.add(word)
                    if word in count:
                        count[word] += 1
                    else:
                        count[word] = 1
        # Heap to store  count and key and get the max count 
        # Space 0(k)
        heap = []
        # Time - O(k)
        for key, value in count.items():
            # Time - O(log k)
            heapq.heappush(heap, (-value, key))
        # Time - O(k log k)
        return [heapq.heappop(heap) for i in range(k)]


if __name__ == "__main__":
    s = Solution()
    k = 2
    keywords = ["anacell", "cetracular", "betacellular"]
    reviews = [
        "Anacell provides the best services in the city",
        "betacellular has awesome services",
        "Best services provided by anacell, everyone should use anacell",
    ]
    print(s.TopK(keywords, reviews, k))

    k = 2
    keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
    reviews = [
        "I love anacell Best services; Best services provided by anacell",
        "betacellular has great services",
        "deltacellular provides much better services than betacellular",
        "cetracular is worse than anacell",
        "Betacellular is better than deltacellular.",
    ]
    print(s.TopK(keywords, reviews, k))
