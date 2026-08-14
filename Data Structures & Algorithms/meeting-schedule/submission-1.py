"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        l = len(intervals)
        if l <=1:
            return True
        intervals.sort(key=lambda pair:pair.start)
        curr = intervals[0]
        for i in range(1,l):
            if curr.end > intervals[i].start:
                return False
            curr = intervals[i]
        return True