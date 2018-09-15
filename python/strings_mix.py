import string


def mix(s1, s2):
    dict1 = weight(s1)
    dict2 = weight(s2)

    ret = []

    print(dict1, dict2)

    print(list(set(dict1.keys()).intersection(dict2.keys())))

    for i in list(set(dict1.keys()).union(dict2.keys())):
        if i not in dict2.keys():
            a = "1:" + i*dict1[i]
            ret.append(a)
        elif i not in dict1.keys():
            a = "2:" + i*dict2[i]
            ret.append(a)
        elif dict1[i] > dict2[i]:
            a = "1:" + i*dict1[i]
            ret.append(a)

        elif dict2[i] > dict1[i]:
            a = "2:" + i*dict2[i]
            ret.append(a)

        elif dict1[i] == dict2[i] and dict1[i] > 1:
            a = "=:" + i*dict1[i]
            ret.append(a)


    print(ret)
    ret = sorted(ret, key= lambda a:(len(a), (-1) * ord(a[0]), (-1) * ord(a[2])), reverse=True)
    return "/".join(i for i in ret)


def weight(s):
    d = {}
    for i in set(s):
        if i in string.ascii_lowercase\
           and s.count(i) > 1:
            d[i] = s.count(i)

    return d
