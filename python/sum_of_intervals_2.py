def sum_of_intervals(intervals):
    intervals = sorted(list(set(intervals)))
    ix = 0
    while ix < len(intervals) - 1:
        if len(intervals) > 2 and \
           overlap(intervals[ix], intervals[ix+1]):
            y = union_(intervals[ix], intervals[ix+1])
            del intervals[ix:ix+2]
            intervals.insert(ix, y)

        else:
            ix += 1

    if len(intervals) >= 2 and \
       overlap(intervals[-2], intervals[-1]):
        y = union_(intervals[-2], intervals[-1])
        del intervals[-2:]
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


