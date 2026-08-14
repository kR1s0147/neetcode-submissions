class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        n = 0

        while  n < len(intervals) and  intervals[n][1] < newInterval[0]:
            res.append(intervals[n])
            n+=1
        while n < len(intervals) and newInterval[1] >= intervals[n][0]:
            newInterval[0] = min(newInterval[0],intervals[n][0])
            newInterval[1] = max(newInterval[1],intervals[n][1]) 
            n+=1
        res.append(newInterval)
        while n < len(intervals):
            res.append(intervals[n])
            n+=1
        return res