def solution(number):
    s = 0
    for i in range(1, number):
        if (i%3==0 or i%5==0):
            s += i
    return s

if __name__ == "__main__":
    print(solution(10))
    
