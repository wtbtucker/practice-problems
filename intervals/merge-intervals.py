'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Test Cases:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def areOverlapping(a: List[int], b: List[int]) -> bool:
            return a[0] <= b[1] and b[0] <= a[1]
        
        def mergeIntervals(a: List[int], b: List[int]) -> List[int]:
            start = min(a[0], b[0])
            end = max(a[1], b[1])
            return [start, end]

        sorted_intervals = sorted(intervals, key= lambda x: x[0])
        answer = [sorted_intervals[0]]


        for i in range(1, len(sorted_intervals)):
            if areOverlapping(sorted_intervals[i], answer[-1]):
                answer[-1] = mergeIntervals(sorted_intervals[i], answer[-1])
            else:
                answer.append(sorted_intervals[i])
        
        return answer