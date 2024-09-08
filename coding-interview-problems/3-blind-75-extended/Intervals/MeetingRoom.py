''''
Problem:  Given interval, determine if is there any conflict while scheduling meeting.

intervals = [(0,30),(5,10),(15,20)]


Steps:
1. Sort the intervals 
2. compare if curIntervalEnd <= nextIntervalStart -> return True ; else False

TC : O(nlogn)
TC : O(n)
'''



class Solution:
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key=lambda x:x[0])
        print(intervals)
        curInterval = intervals[0]
        for nextInterval in intervals:
            _ , curIntervalEnd = curInterval
            nextIntervalStart, nextIntervalEnd = nextInterval


            print(curIntervalEnd, nextIntervalEnd)

            # there is conflict
            if curIntervalEnd < nextIntervalStart:
                return False
            curInterval = nextInterval
        return True



intervals = [(0,30),(5,10),(15,20)] # False
# intervals = [(5,8),(9,15)] - True
sl = Solution()
print(sl.canAttendMeetings(intervals))