def solution(args):
    soln = []
    for ix, i in enumerate(args):
        try:
            __import__('pudb').set_trace()
            if not args[ix+1] == i+1:
                if ('b' not in locals() or i!=b):
                    soln.append(i)
                if 'x' in locals() and 'b' in locals():
                    if b-x != 1:
                        soln.append("-".join(str(j) for j in (x, b)))
                    else:
                        soln.append(x)
                        soln.append(b)
                x = args[ix+1]
            else:
                if 'b' not in locals():
                    soln.append(i)
                b = args[ix+1]
        except IndexError:                 
            print("List Traverse Complete")

    soln.append("-".join(str(j) for j in (x, b)))
    return ",".join(str(y) for y in soln)

