def maxSequence(arr):
    if arr == []:
        return 0
    max_so_far = max_ending_here = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_ending_here, max_so_far)

    if max_so_far>=0:
        return max_so_far
    else:
        return 0
	

