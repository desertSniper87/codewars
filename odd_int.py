def find_it(seq):
    res = []
    for i in seq:
       if i not in res:
           res.append(i)
       else:
           res.remove(i)
    return res[0]

if __name__ == "__main__":
    x = find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
    print(x)

