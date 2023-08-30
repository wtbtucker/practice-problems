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

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = None
    

class Solution:
    def __init__(self):
        self.answer = []

    def dfs(self, root, cell, board):
        if root:
            ret = []
            if root.word:
                ret.append(root.word)
            
            row, col = cell
            letter = board[row][col]
            board[row][col] = '$'
            for adjacent_cell in self.findAdjacentCells(cell, board):
                r, c = adjacent_cell
                if board[r][c] in root.children:
                    ret.extend(self.dfs(root.children[board[r][c]], adjacent_cell, board))
            board[row][col] = letter
            
        return ret
        
    def findAdjacentCells(self, cell, board):
        adjacent_cells = []
        r, c = cell
        if r-1 >= 0:
            adjacent_cells.append((r-1, c))
        if r+1 < len(board):
            adjacent_cells.append((r+1, c))
        if c-1 >= 0:
            adjacent_cells.append((r, c-1))
        if c+1 < len(board[0]):
            adjacent_cells.append((r, c+1))
            
        return adjacent_cells
        
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        curr = root
        
        # Insert words into Trie
        for word in words:
            for ch in word:
                curr = curr.children[ch]
            curr.word = word
            curr = root
            
        
        answer = []
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell in root.children:
                    answer.extend(self.dfs(root.children[cell], (i, j), board))
        return set(answer)
        