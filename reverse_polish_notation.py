#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 27.01.2018
# Last Modified Date: 28.01.2018
# Completed         : 27.01.2018

# https://en.wikipedia.org/wiki/Reverse_Polish_notatifor each token in the postfix expression:
# for each token in the postfix expression:
# if token is an operator:
    # operand_2 ← pop from the stack
    # operand_1 ← pop from the stack
    # result ← evaluate token with operand_1 and operand_2
    # push result back onto the stack
# else if token is an operand:
    # push token onto the stack
    # result ← pop from the stackon

def operation(s, o1, o2):
    if s=='+':
        return o1+o2
    elif s=='-':
        return o1-o2
    elif s=='*':
        return o1*o2
    elif s=='/':
        return o1/o2

def calc(expr):
    print(expr)
    if (expr==""): return '0'
    notation = expr.split(" ")
    stack = []
    result = []
    for token in notation:
        if token.replace('.', '1').isdigit()==False:
            o2 = stack.pop()
            o1 = stack.pop()
            result = operation(token, int(o1), int(o2))
            stack.append(result)
        else:
            stack.append(token)
    print(stack[-1])
    a = stack[-1]
    try: 
        return float(a)
    except:
        return int(a)


if __name__ == "__main__":
    calc("")
    calc("1 2 3")
    calc("1 2 3.5")
    calc("1 3 +")
    calc("1 3 *")
    calc("1 3 -")
    calc("4 2 /")
