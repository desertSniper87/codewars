def digital_root(n):
    r = 0
    for i in str(n):
        r += int(i)
    if (r>10):
        return digital_root(r)
    return r

if __name__ == "__main__":
    print(digital_root(16))
    print(digital_root(942))
    print(digital_root(132189))
    print(digital_root(493193))
    
    
