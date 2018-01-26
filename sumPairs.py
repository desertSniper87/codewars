l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

def sum_pairs(ints, s):
    # print(ints)
    pair = None
    pair_index = 9999
    for index_i, i in enumerate(ints):
        temp_list = ints[index_i:]
        for index_j, j in enumerate(ints):
            if index_j!=index_i and index_i>index_j:
                if i+j == s:
                    index = max(index_i, index_j)
                    if pair_index>index:
                        pair = [j, i]
                        pair_index = index
                        if index_i==0 and index_j==1:
                            return pair
                        # print("i, j",i, j)
                        # print("index_i, index_j", index_i, index_j)
                        # print(pair_index)
    return pair

# def sum_pairs(ints, s):
    # pair_index = 99999
    # for index_i, i in enumerate(ints):
        # # print("i", i)
        # temp_list = ints[:]
        # temp_list.remove(i)
        # for index_j, j in enumerate(temp_list):
            # print("i, j",i, j)
            # if i+j == s:
                # print("pair index:", pair_index)
                # print("ints.index(i), ints.index(j)", index_i, index_j)
                # index = min(index_i, index_j)
                # if index< pair_index:
                    # pair = [i, j]
                    # pair_index = index

    # return pair

if __name__ == "__main__":
    # print sum_pairs(l1, 8)
    # print sum_pairs(l2, -6)
    print sum_pairs(l3, -7)
    # print sum_pairs(l5, 10)





