def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    result = list()

    # if there are intervals to merge, then return an empty list
    if len(intervals) <= 0:
        return result
    
    # sort intervals by start time
    intervals.sort(key = lambda i: i[0])
    
    # iterate through intervals, looking for overlapping intervals
    currStart = intervals[0][0]
    currEnd = intervals[0][1]
    i = 1
    while i < len(intervals):
        # an overlapping interval is one that does NOT start after the
        # previous one ended
        if intervals[i][0] <= currEnd:
            # the currEnd variable stores the last ending time seen for
            # overlapping intervals
            currEnd = max(currEnd, intervals[i][1])
        else:
            # if we find a non-overlapping interval, then we add the previous
            # coagulated interval to result
            result.append([currStart, currEnd])
            # reset currStart and currEnd variables to catch a new run
            # of overlapping intervals
            currStart = intervals[i][0]
            currEnd = intervals[i][1]
        
        # move to next interval
        i += 1
        
    # add the leftover interval that hasn't been put into result yet
    result.append([currStart, currEnd])
    return result