from itertools import product

def get_pins(observed):
    '''TODO: This is your job, detective!
    ┌───┬───┬───┐
    │ 1 │ 2 │ 3 │
    ├───┼───┼───┤
    │ 4 │ 5 │ 6 │
    ├───┼───┼───┤
    │ 7 │ 8 │ 9 │
    └───┼───┼───┘
        │ 0 │
        └───┘
        '''
    neighbour_dict = {
                      '0': ['0', '8'],
                      '1': ['1', '2', '4'],
                      '2': ['2', '1', '3', '5'],
                      '3': ['3', '2', '6'],
                      '4': ['4', '1', '5', '7'],
                      '5': ['5', '2', '4', '6', '8'],
                      '6': ['6', '3', '5', '9'],
                      '7': ['7', '4', '8'],
                      '8': ['8', '5', '7', '9', '0'],
                      '9': ['9', '8', '6'],
                     }

    p = [ neighbour_dict[i] for i in observed ]

    res = []
    for i in product(*p):
        res.append("". join(x for x in i))

    return res

