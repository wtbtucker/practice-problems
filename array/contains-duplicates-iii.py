'''
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.

Test Cases:
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true

Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false

Constraints:
2 <= nums.length <= 105
-109 <= nums[i] <= 109
1 <= indexDiff <= nums.length
0 <= valueDiff <= 109
'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        def getBucketID(num, valueDiff):
            return num // valueDiff if valueDiff > 0 else num

        buckets = {}

        for i, num in enumerate(nums):
            bucket_id = getBucketID(num, valueDiff)

            # Another value is same bucket is guaranteed to be within valueDiff
            if bucket_id in buckets:
                return True

            for delta_id in [-1, 1]:
                if (bucket_id + delta_id) in buckets and abs(num - buckets[bucket_id + delta_id]) <= valueDiff:
                    return True
            
            buckets[bucket_id] = num

            # i is increasing as we iterate through so rightmost bucket will never satisfy indexDiff
            if i >= indexDiff:
                rightmost_value = nums[i - indexDiff]
                rightmost_bucket_id = getBucketID(rightmost_value, valueDiff)
                del buckets[rightmost_bucket_id]
            
        return False