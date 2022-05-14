'''
-- Merge Overlapping Intervals 
  intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
  expected = [[1, 2], [3, 8], [9, 10]]

  TC : O(n log(n))
  SC : O(N)

  Algorithm :
  1. Sort given Interval by start value of merge interval 
  2. Now add first interval into output array (atlease one interval which is not overlapping)
  3. Loop through sorted interval and compare 
    if (currentIntervalEnd >= nextIntervalStart)
        > Then Modify current element end value with max(urrentIntervalEnd, nextIntervalEnd)
    else :
        > directly add interval in the output array
'''


def mergeOverlappingIntervals(intervals):
    # sort intervals by value of first ele of intervals
    sortedIntervals = sorted(intervals, key=lambda x:x[0])

    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval 

        # if this not satisfy then directly add interval into merged interval array.
        if(currentIntervalEnd >= nextIntervalStart):
                currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)

    return mergedIntervals



if __name__ == "__main__":
    intervals = [
        [1, 2],
        [3, 5],
        [4, 7],
        [6, 8],
        [9, 10]
    ]

    ans = mergeOverlappingIntervals(intervals)
    print(ans)
