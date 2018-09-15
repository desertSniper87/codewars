def sum_of_intervals(intervals):
    print(intervals)
    intervals = sorted(list(set(intervals)))
    ix = 0
    sum_ = 0
    lower_bound = 0
    __import__('pudb').set_trace()
    while(len(intervals) > 0):
        # intervals = sorted(list(set(intervals)))
        if len(intervals) > 1:
            if intervals[ix][1] > intervals[ix+1][0]:
                sum_ += intervals[ix][1] - intervals[ix][0]
                if intervals[ix+1][1] > intervals[ix][1]:
                    intervals.insert(2, (intervals[ix][1], intervals[ix+1][1]))
                    lower_bound = max(intervals[ix][1], intervals[ix+1][1])
                del intervals[ix+1]
                del intervals[ix]
            else:
                sum_ += intervals[ix][1] - max(intervals[ix][0], lower_bound)
                del(intervals[ix])
        else:
                sum_ += intervals[-1][1] - max(intervals[-1][0], lower_bound)
                del(intervals[ix])

    return sum_
