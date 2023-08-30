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
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = sum(nums)
        if total_sum % 2:
            return False

        target = total_sum // 2
        n = len(nums)

        @cache
        def dp(idx: int, remaining: int) -> bool:
            if remaining == 0:
                return True
            
            if remaining < 0 or idx < 0:
                return False
            
            return dp(idx - 1, remaining) or dp(idx - 1, remaining - nums[idx])
        
        return dp(n-1, target)
        
