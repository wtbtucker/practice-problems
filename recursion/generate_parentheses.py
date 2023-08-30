'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Test Cases:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memo = {0: ['']}

        def dp(i):
            if i in memo:
                return memo[i]
            
            level = []
            for left_count in range(i):
                for left_string in dp(left_count):
                    for right_string in dp(i - 1 - left_count):
                        level.append('(' + left_string + ')' + right_string)
            
            memo[i] = level
            return memo[i]
        
        
        return dp(n)
        