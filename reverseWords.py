# def reverse(st):
    # rev_st = ""
    # x = ""
    # for i in st:
        # if i == ' ':
            # rev_st += x[::-1]+' '
            # x = ''
        # else:
            # x += i
    # rev_st += x[::-1]
    # return rev_st[::-1]

def reverse(st):
    l = st.split(' ')
    r = ""
    for i in reversed(l):
        r += i
        r += ' '

    return r[:len(r)-1]

 # def reverse(st):
    # return ' '.join(st.split(' ')[::-1])   


if __name__ == '__main__':
    print reverse('hello there')
    print reverse('hsktuwp t suqelgfl')
