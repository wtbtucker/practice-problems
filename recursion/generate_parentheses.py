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
        answer = []

        def backtrack(cur_string, left_count, right_count): 
            if len(cur_string) == 2*n:
                answer.append(''.join(cur_string))
                return
            if left_count < n:
                cur_string.append('(')
                backtrack(cur_string, left_count + 1, right_count)
                cur_string.pop()
            if right_count < left_count:
                cur_string.append(')')
                backtrack(cur_string, left_count, right_count + 1)
                cur_string.pop()
        
        backtrack([], 0, 0)
        return answer
        
        