'''
Given an array of unique strings words, return all the word squares you can build from words. The same word from words can be used multiple times. You can return the answer in any order.

A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 4
All words[i] have the same length.
words[i] consists of only lowercase English letters.
All words[i] are unique.

Test Cases:
Input: words = ["area","lead","wall","lady","ball"]
Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]

Input: words = ["abat","baba","atan","atal"]
Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
'''
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = None

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.word_length = len(words[0])
        results = []
        word_squares = []

        self.buildTrie(words)
        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results

    def buildTrie(self, words):
        self.root = TrieNode()

        for word in words:
            node = self.root
            for ch in word:
                node = node.children[ch]
            node.word = word
    
    def backtracking(self, step, word_squares, results):
        if step == self.word_length:
            results.append(word_squares[:])
            return
        
        prefix = ''.join([word[step] for word in word_squares])
        for candidate in self.getWordsWithPrefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()
        
    def getWordsWithPrefix(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return []
            curr = curr.children[ch]
        return self.dfs(curr)

    def dfs(self, root):
        ret = []
        if root:
            if root.word:
                ret.append(root.word)
            for child in root.children:
                ret.extend(self.dfs(root.children[child]))
        return ret