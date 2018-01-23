# https://www.codewars.com/kata/english-beggars/train/python

def beggars(values, n):  # n = beggers, values = List of begs
    if n==0:
        return []
    beg_list = [0] * n
    for i in range(0, len(values)):
        beg_list[i%n] += values[i]

    print(beg_list)


if __name__ == '__main__':
    beggars([1, 2, 3, 4, 5], 0)
