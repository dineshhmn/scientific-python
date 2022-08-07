"""
Design a data structure that will be initialized with a string array,
 and then it should answer queries of the shortest distance between two different strings from the array.

Implement the WordDistance class:

WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.

Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1
"""

class WordDistance:
    def __init__(self, wordsDict):
        self.wordsDict = self.make_dict(wordsDict)

    def make_dict(self, words):
        ret_val = {}
        for i in range(len(words)):
            if words[i] in ret_val.keys():
                ret_val[words[i]].append(i)
            else:
                ret_val[words[i]] = [i]
        print(ret_val)
        return ret_val

    def shortest(self, word1, word2):
        if (word1 or word2):
            ret_val = []
            a = self.wordsDict.get(word1, 0)
            b = self.wordsDict.get(word2, 0)
            for i in a:
                for j in b:
                    ret_val.append(i - j)
            return min(ret_val)

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

if __name__ == "__main__":
    x = [[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
    s = WordDistance(x[0])
    print(s.shortest(x[1][0], x[1][1]))
    print(s.shortest(x[2][0], x[2][1]))

