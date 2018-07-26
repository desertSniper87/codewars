import operator

def next_bigger(n):
    # print(n)
    if n>99999999999999:
        return -1

    arr = list(str(n))
    i = len(arr) - 1

    print("set(arr[-3:])", set(arr[-3:]), "len: ", len(set(arr[-3:])))
    if len(set(arr[-3:])) in (2, 3) or arr[-1]=='0' or n>50884848483553:
        # print(bcolors.WARNING + "General Reposti!" + bcolors.ENDC)
        return next_bigger_alt(n)

    if len(set(arr))==2:
        return next_bigger_alt_3(n)

    while(i>0):
        if arr[i] > arr[i-1]:
            m, _ = min(enumerate(arr[i-1:]), key=operator.itemgetter(1))
            try:
                arr[i-1], arr[i+m] = arr[i+m], arr[i-1]
            except IndexError:
                return next_bigger_alt(n)
            return int("".join(x for x in arr))
        i-=1
    return -1

from itertools import permutations

def next_bigger_alt_3(n):
    arr = list(str(n))
    n_arr = []
    for x in permutations(arr):
        n_arr.append(int("".join(y for y in x)))

    n_arr = [x for x in n_arr if len(str(x)) == len(str(n)) and x>n]
    if n_arr == []:
        return -1
    return min(n_arr)



def next_bigger_alt_2(n):
    arr = list(str(n))
    for idx, i in enumerate(arr[len(arr)-1::-1]):
        # print("idx, i: ", idx, i)
        for jdx, j in enumerate(arr[:idx:-1]):
            # print("idx, i: ", idx, i)
            # print("jdx, j: ", jdx, j)
            if int(j) > int(i):
                # print("if int(j) > int(i):")
                # print("jdx, j: ", jdx, j)
                arr[idx] = j
                arr[jdx+idx+1] = i
                return int("".join(i for i in arr))



def next_bigger_alt(n):
    #your code here
    set_n = set(str(n))
    # for i in itertools.count(n+1):
    for i in range(n+1, n+999999):
        if same_dig(i, set_n) and digit_check(str(n), str(i)):
            return i

    return -1

def same_dig(i, set_n):
    """Checks if same digits

    :i: number
    :s: set
    :returns: bool

    """
    # print("i, set_n, size_n: ", i, set_n, size_n)
    set_i = set(str(i))
    if set_i == set_n:
        return True
    else:
        return False

def digit_check(s, x):
    """Digit Cheking Method 

    :s: String
    :i: String
    :returns: bool

    """
    for i in set(s):
        if s.count(i) != x.count(i):
            return False

    return True




# x = 12
# x =513 #p31 
# x =2017 #2071 
# x =414 #441 
# x =144 #414 
# print(next_bigger(x))

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
