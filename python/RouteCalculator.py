# from itertools import chain
import re

def calculate(expression):
    digits = re.split('\D+', expression)
    operators = re.findall('[\+\-\*\$\.]+', expression, re.DOTALL)
    res = 0
    stack = []
    for i, j, k in zip(digits[0::2], digits[1::2], operators):
        # print(i, j, k)
        if len(digits) == 1:
            return digits[0]
        elif k == '.':
            res += float( i + '.' + j )
        elif k == '$':
            res += int(i) // int(j)
        elif k == '*':
            if '$' not in operators:
                res += int(i) * int(j)
            else:
                stack.append(i)
                stack.append(j)
        elif k == '-':
            if '*' or '$' not in operators:
                res += int(i) - int(j)
            else:
        elif k == '+':
            res += int(i) + int(j)
                
    # print(digits, operators)
    return res
