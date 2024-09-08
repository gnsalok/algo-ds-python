'''
Meeting Room II

Problem : Given array of meeting consisting start and end times. 
Find the minimum no. of conference rooms required.

'''


class Solution:
    def minMeetingRooms(self, intervals):
        result, count = 0, 0
        sorted(intervals, key=lambda x:x[0])
        curInterval = intervals[0]

        for nextInterval in intervals:
            _, curIntervalEnd = curInterval
            nextIntervalStart, nextIntervalEnd = nextInterval
            if curIntervalEnd > nextIntervalStart:
                count += 1
            else:
                count -= 1
            curInterval = nextInterval
            result = max(count, result)
        return result


intervals = [(0,30),(5,10),(11,15)]
sl = Solution()
print(sl.minMeetingRooms(intervals)) #  2