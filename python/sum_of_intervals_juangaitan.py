def sum_of_intervals(intervals):
    (min, max), *sorted_intervals = sorted(intervals)
    sum = max - min
    for a, b in sorted_intervals:
        if b > max:
            rest = max - a if max > a else 0
            sum += b - a - rest
            max = b
    return sum
