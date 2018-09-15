def order_weight(string):
    num_list = string.split(' ')
    return " ".join(str(i) for i in sorted(num_list, key= lambda x : \
                                           (weight_function(x), x)))


def weight_function(number_string):
    return sum(int(i) for i in number_string)

