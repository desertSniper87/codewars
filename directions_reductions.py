def dirReduc(arr):
    #TODO Make custom test cases and then submit
    back = {
            "NORTH": "SOUTH",
            "SOUTH": "NORTH",
            "EAST" : "WEST",
            "WEST" : "EAST"
           }
    result = []
    for i in a:
        if len(result)!=0 and result[-1]==back[i]:
            result.remove(back[i])
        else:
            result.append(i)
    # if len(result)==2:
        # return [result[1], result[0]]
    return result

if __name__ == "__main__":
    # a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    a=["NORTH", "WEST", "SOUTH", "EAST"]
    x = dirReduc(a)
    print(x)
