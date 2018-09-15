def accum(s):
    res = []
    for idx, i in enumerate(s):
        res.append(i.upper() + i.lower()*(idx))
    
    return "-".join(i for i in res)

