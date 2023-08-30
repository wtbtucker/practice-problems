'''
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').

You are given a string array sentences and an integer array times both of length n where sentences[i] is a previously typed sentence and times[i] is the corresponding number of times the sentence was typed. For each input character except '#', return the top 3 historical hot sentences that have the same prefix as the part of the sentence already typed.

Constraints:
n == sentences.length
n == times.length
1 <= n <= 100
1 <= sentences[i].length <= 100
1 <= times[i] <= 50
c is a lowercase English letter, a hash '#', or space ' '.
Each tested sentence will be a sequence of characters c that end with the character '#'.
Each tested sentence will have a length in the range [1, 200].
The words in each input sentence are separated by single spaces.
At most 5000 calls will be made to input.

Test-cases:
Input
["AutocompleteSystem", "input", "input", "input", "input"]
[[["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2]], ["i"], [" "], ["a"], ["#"]]
Output
[null, ["i love you", "island", "i love leetcode"], ["i love you", "i love leetcode"], [], []]
'''
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
        self.data = None
        self.rank = 0
        
class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.keyword = ""
        for sentence, times_entered in zip(sentences, times):
            self.addRecord(sentence, times_entered)

    def addRecord(self, sentence, times_entered):
        curr = self.root
        for char in sentence:
            curr = curr.children[char]
        curr.is_word = True
        curr.data = sentence
        curr.rank -= times_entered
    
    def dfs(self, root):
        ret = []
        if root:
            if root.is_word:
                ret.append((root.rank, root.data))
            for child in root.children:
                ret.extend(self.dfs(root.children[child]))
        return ret
        
    def search(self, sentence):
        curr = self.root
        for char in sentence:
            if char not in curr.children:
                return []
            curr = curr.children[char]
        return self.dfs(curr)
    
    # accept stream of user input character by character, store in global variable
    def input(self, char):
        results = []
        if char != "#":
            self.keyword += char
            results = self.search(self.keyword)
        
        # store input in Trie
        else:
            self.addRecord(self.keyword, 1)
            self.keyword = ""
        return [item[1] for item in sorted(results)[:3]]