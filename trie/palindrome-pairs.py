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

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        # valid prefix word[:i] means word[i:] is palindromic
        def all_valid_prefixes(word):
            valid_prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefixes.append(word[:i])
            return valid_prefixes
        
        # valid suffix word[i:] means word[:i] is palindromic
        def all_valid_suffixes(word):
            valid_suffixes = []
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    valid_suffixes.append(word[i+1:])
            return valid_suffixes
        
        word_lookup = {word: i for i, word in enumerate(words)}
        solutions = []

        for idx, word in enumerate(words):

            # case where reversed_word exactly equals another word 
            # eg. cat + tac
            reversed_word = word[::-1]
            if reversed_word in word_lookup and idx != word_lookup[reversed_word]:
                solutions.append([idx, word_lookup[reversed_word]])
            
            # case where prefix of word matches another word and remainder of word is palindromic 
            # eg cataba + tac
            for prefix in all_valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_lookup:
                    solutions.append([idx, word_lookup[reversed_prefix]])
            
            # case where suffix of word matches another word and remainder of word is palindromic
            # eg lls + sssll
            for suffix in all_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_lookup:
                    solutions.append([word_lookup[reversed_suffix], idx])
        
        return solutions