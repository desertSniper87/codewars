def sum_of_intervals(intervals):
    intervals = sorted(list(set(intervals)))



    try:
        for ix, i in enumerate(intervals):
            if overlap(i, intervals[ix+1]):
                y = union_(i, intervals[ix+1])
                del intervals[ix]
                del intervals[ix]
                intervals.insert(ix, (0, 0))
                intervals.insert(ix+1, y)
    except IndexError:
        if overlap(intervals[0], intervals[-1])\
           and len(intervals) > 1:
            y = union_(intervals[0], intervals[-1])
            del intervals[0]
            del intervals[-1]
            intervals.insert(ix, y)

    print(intervals)

    sum_ = 0
    for i in intervals:
        sum_ += i[1] - i[0]

    return sum_




def union_(i1, i2):
   return (min(i1[0], i2[0]), max(i1[1], i2[1]))


def overlap(i1, i2):
    if i2[0] < i1[1]:
        return True
    return False


