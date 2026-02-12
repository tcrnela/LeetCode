class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        ans = 0
        a = intervals[0][1]
        for i in range (1, len(intervals)):
            if intervals[i][0] >= a:
                a = intervals[i][1]
            else:
                ans += 1
        return ans