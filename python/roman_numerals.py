class RomanNumerals(object):
    def to_roman(n):
        M = n // 1000
        m = n % 1000
        D = m // 500
        d = m % 500
        C = d // 100
        c = d % 100
        L = c // 50
        l = c % 50
        X = l // 10
        x = l % 10
        V = x // 5
        v = x % 5
        IV = v // 4
        iv = v % 4
        I = iv 

        print("I: ", I)
        print("IV: ", IV)
        print("iv: ", iv)
        print("V: ", V)
        print("v: ", v)
        print("X: ", X)
        print("x: ", x)
        print("L: ", L)
        print("l: ", l)
        print("C: ", C)
        print("c: ", c)
        print("D: ", D)
        print("d: ", d)
        print("M: ", M)
        print("m: ", m)

        soln = ""
        soln += 'M'*M
        soln += 'D'*D
        soln += 'C'*C
        soln += 'L'*L
        soln += 'X'*X
        soln += 'V'*V
        soln += 'IV'*IV
        soln += 'I'*I
        return soln
