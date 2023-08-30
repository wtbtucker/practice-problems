'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Test Cases:
Input: n = 2
Output: [0,1,1]

Input: n = 5
Output: [0,1,1,2,1,2]

Constraints:
0 <= n <= 105
'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = [0 for _ in range(n+1)]
        x = 0
        power_two = 1

        while power_two <= n:
            while x < power_two and x + power_two <= n:
                ans[x + power_two] = ans[x] + 1
                x += 1
            x = 0
            power_two <<= 1
        

        return ans