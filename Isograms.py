def is_isogram(string):
    # for c in string:
    # print (c)
    i = 0
    dict = {}
    for c in string:
        if c == 'O':
            c = 'o'
        if c not in dict:
            dict[c] = 0
        dict[c]+=1

        if dict[c]>1:
            return False
    return True

# def is_isogram(string):
#     x = len(string)
#     y = string.lower()
#     z = set(y)
#     w = len(z)
#     return len(string) == len(set(string.lower()))

if is_isogram("moSse"):
    print ("yea")
else:
    print("nya")
