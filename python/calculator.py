import string


class Calculator(object):
    def evaluate(self, string):
        print(string)

        tokens = string.split(" ")
        if len(tokens) == 1:
            return float(tokens[0])

        for ix, i in enumerate(tokens):
            if i == '*':
                a1 = float(tokens[ix-1])
                a2 = float(tokens[ix+1])
                tokens[ix] = a1*a2
                del tokens[ix-1]
                ix -= 1
                del tokens[ix+1]
        print(tokens)

        for ix, i in enumerate(tokens):
            if i == '/':
                a1 = float(tokens[ix-1])
                a2 = float(tokens[ix+1])
                tokens[ix] = a1//a2
                del tokens[ix-1]
                ix -= 1
                del tokens[ix+1]
        print(tokens)

        for ix, i in enumerate(tokens):
            if i == '-':
                a1 = float(tokens[ix-1])
                a2 = float(tokens[ix+1])
                tokens[ix] = a1-a2
                del tokens[ix-1]
                ix -= 1
                del tokens[ix+1]
        print(tokens)

        for ix, i in enumerate(tokens):
            if i == '+':
                a1 = float(tokens[ix-1])
                a2 = float(tokens[ix+1])
                tokens[ix] = a1+a2
                del tokens[ix-1]
                ix -= 1
                del tokens[ix+1]

        return tokens[0]
