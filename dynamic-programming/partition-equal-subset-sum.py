'''
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Test Cases:
Input: nums = [1,5,11,5]
Output: true

Input: nums = [1,2,3,5]
Output: false

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
'''
from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 == 1:
            return False

        target = total // 2

        n = len(nums)
        
        @lru_cache(None)
        def dfs(nums: Tuple[int], n: int, target: int) -> bool:
            if target == 0:
                return True
            if n == 0 or target < 0:
                return False
            
            result = dfs(nums, n-1, target) or dfs(nums, n-1, target-nums[n-1])
            return result
        
        return dfs(tuple(nums), n-1, target)