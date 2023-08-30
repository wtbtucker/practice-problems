'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

Test Cases:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)

        # binary search in the smaller array to reduce overall time complexity
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        left, right = 0, m

        # for even number of elements find smaller of two middle elements
        median_idx = (m + n + 1) // 2 

        while left <= right:
            partition_1 = (left + right) // 2
            partition_2 = median_idx - partition_1
            
            max_left_1 = nums1[partition_1 - 1] if partition_1 > 0 else -float('inf')
            min_right_1 = nums1[partition_1] if partition_1 < m else float('inf')

            max_left_2 = nums2[partition_2 - 1] if partition_2 > 0 else -float('inf')
            min_right_2 = nums2[partition_2] if partition_2 < n else float('inf')

            # partition_1 and partition_2 are in the middle of the entire search space
            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                if (m + n) % 2:
                    return max(max_left_1, max_left_2)
                else:
                    return (max(max_left_1, max_left_2) + min(min_right_1, min_right_2)) / 2

            # too many elements are greater than partition elements
            elif max_left_1 > min_right_2:
                right = partition_1 - 1
            
            # too many elements are less than partition elements
            else:
                left = partition_1 + 1
