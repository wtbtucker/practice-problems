'''
You are given a 0-indexed array of unique strings words.

A palindrome pair is a pair of integers (i, j) such that:

0 <= i, j < words.length,
i != j, and
words[i] + words[j] (the concatenation of the two strings) is a palindrome.
Return an array of all the palindrome pairs of words.

Constraints:
1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lowercase English letters.

Test Cases:
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]

Input: words = ["a",""]
Output: [[0,1],[1,0]]
'''

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_idx = None
        self.palindrome_suffixes = []

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        self.words = words
        self.buildTrie(self.words)
        answer = []
        for i, word in enumerate(words):
            answer.extend(self.searchWord(i, word))
        return answer
            

    def buildTrie(self, words):
        self.root = TrieNode()
        for i, word in enumerate(words):
            curr = self.root
            for j, ch in enumerate(word):
                if word[j:] == word[j:][::-1]:
                    curr.palindrome_suffixes.append(i)
                curr = curr.children[ch]
            curr.word_idx = i

    def searchWord(self, i, word):
        m = len(word)
        
        curr = self.root
        palindromes = []
        
        for j in range(m-1,-1,-1):
            if curr.word_idx != None and (word[:j+1] == word[:j+1][::-1]):
                if curr.word_idx != i:
                    palindromes.append([curr.word_idx, i])
            ch = word[j]
            if ch not in curr.children:
                return palindromes
            curr = curr.children[ch]

        if curr.word_idx != None and curr.word_idx != i:
            palindromes.append([curr.word_idx, i])
        for j in curr.palindrome_suffixes:
            palindromes.append([j, i])          
        
        return palindromes
            
            