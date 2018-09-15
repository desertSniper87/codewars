from math import sqrt, ceil
from operator import itemgetter
def sum_for_list(lst):
    prime_dict = {}
    res = {}
    total_primes = set()

    for i in lst:
        l = prime_factor_list(i)
        prime_dict[i] = l
        for i in l:
            total_primes.add(i)

    for i in total_primes:
        res[i] = 0

    for i in total_primes:
        for j in prime_dict:
            if i in prime_dict[j]:
                res[i] += j * lst.count(j)

    sorted_res = sorted(res.items(), key=itemgetter(0))

    return [[k, v] for (k, v) in  sorted_res]



def prime_factor_list(number):
    """TODO: Docstring for prime_factor_list.

    :number: int
    :returns: list
    the list of the prime factor of the number

    """
    l = []
    for i in range(2, (abs(number)) + 1):
        # print("i: ", i)
        if (number % i == 0) and is_prime(i):
            # print(is_prime(number))
            l.append(i)

    return l

def is_prime(n):
    if n>2 and n%2==0:
        return False
    return all ( n % i for i in range(3, int(sqrt(n)) + 1, 2 ))

