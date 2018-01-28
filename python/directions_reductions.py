from random import randrange
from random import choice

def dirReduc(arr):
    print(arr)
    #TODO Make custom test cases and then submit
    back = {
            "NORTH": "SOUTH",
            "SOUTH": "NORTH",
            "EAST" : "WEST",
            "WEST" : "EAST"
           }
    result = []
    for i in arr:
        print("result, i, back[i]", result, i, back[i])
        if len(result)!=0 and result[-1]==back[i]:
            del result[-1]
        else:
            result.append(i)

    return result

if __name__ == "__main__":
    # a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    a=["NORTH", "WEST", "SOUTH", "EAST"]
    bug = ['NORTH', 'EAST', 'NORTH', 'EAST', 'WEST', 'SOUTH']

    # directions=["NORTH", "WEST", "SOUTH", "EAST"]
    # https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list?rq=1
    # for _ in range(999999999):
    # while(True):
        # p = []
        # x = []
        # for i in range(randrange(20)):                             
            # p.append(choice(directions))
        # x = dirReduc(p)
        # print("~"*120)
        # print(" "*120)
        # print(p, '\n', x)
        # if x==['NORTH', 'NORTH', 'EAST', 'SOUTH']:
            # break
        # print(" "*120)
        # print("~"*120)
        


    print(dirReduc(bug))
