def solution(args):
    soln = []
    stack = []
    for i in args:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] + 1 != i:
            if len(stack) == 2:
                soln.append(",".join(str(x) for x in stack))
                stack = []
            elif len(stack) == 1:
                soln.append(stack.pop())
            else:
                soln.append("-".join(str(x) for x in (stack[0], stack[-1])))
                stack = []
            stack.append(i)
        else:
            stack.append(i)

    if len(stack) >2 :
        soln.append("-".join(str(x) for x in (stack[0], stack[-1])))
    elif len(stack) == 2:
        soln.append(",".join(str(x) for x in stack))
    elif len(stack) == 1:
        soln.append(stack[0])

    return ",".join(str(y) for y in soln)
