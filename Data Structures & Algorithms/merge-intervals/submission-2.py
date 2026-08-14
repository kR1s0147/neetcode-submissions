class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l = len(intervals)
        if  l<=1:
            return intervals
        res = []
        n = 1
        curr = intervals[0]
        while n < l:
            if  curr[1] < intervals[n][0]:
                res.append(curr)
                curr = intervals[n]

            else:
                curr[0] = min(curr[0],intervals[n][0])
                curr[1] = max(curr[1],intervals[n][1])
                
            if n== l-1:
                res.append(curr)
            n+=1

        return res
                