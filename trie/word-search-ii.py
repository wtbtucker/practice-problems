'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.

Test Cases:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
'''

class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.is_word = False
        self.content = ''

class Solution:
    def insert_word(self, word):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.is_word = True
        curr.content = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = Trie()
        self.answer = set()

        for word in words:
            self.insert_word(word)
        
        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r: int, c: int, visited: set, curr: Trie):
            if curr.is_word:
                self.answer.add(curr.content)
            
            
            for delta_r, delta_c in directions:
                new_r, new_c = r + delta_r, c + delta_c
                if 0 <= new_r < m and 0 <= new_c < n and (new_r, new_c) not in visited and board[new_r][new_c] in curr.children:
                    visited.add((new_r, new_c))
                    dfs(new_r, new_c, visited, curr.children[board[new_r][new_c]])
                    visited.remove((new_r, new_c))
        
        visited = set()
        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if char in self.root.children:
                    visited.add((i, j))
                    dfs(i, j, visited, self.root.children[char])
                    visited.remove((i, j))
        
        return list(self.answer)


        