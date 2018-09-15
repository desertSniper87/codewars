def is_triangle(a, b, c):
    l = [a, b, c]
    m1, m2 = float('inf'), float('inf')
    for x in l:
        if x<=m1:
            m1, m2 = x, m1
        elif x<m2:
            m2 = x

    if (m1+m2 > max(l)):
        return True
    else:
        return False




print(is_triangle(1, 2, 2))
print(is_triangle(1, 2, 3))

