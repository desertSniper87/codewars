def pig_it(text):
    res = []
    for i in text.split(" "):
        if i.isalpha():
            r = i[1:] + i[0] + "ay "
            res.append(r)
        else:
            res.append(i)

    res[-1] = res[-1].strip()
    print(res)
    return "".join(i for i in res)


x = "Pig latin is cool" 
print( pig_it(x) )
