'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Test Cases:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        n = len(nums)

        def findTwoSum(i: int):
            lo = i + 1
            hi = n-1
            while lo < hi:
                three_sum = nums[i] + nums[lo] + nums[hi]
                if three_sum == 0:
                    ans.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo -1]:
                        lo += 1
                
                elif three_sum < 0:
                    lo += 1
                else:
                    hi -= 1

        nums.sort()

        # need at least one negative number or three zeros
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            # make sure we haven't already done the operation on val1
            if i == 0 or nums[i-1] != nums[i]:
                findTwoSum(i)
        
        return ans