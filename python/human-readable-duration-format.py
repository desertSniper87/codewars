def format_duration(seconds):
    #your code here
    if seconds == 0:
        return "now"

    y = seconds // (365 * 60 * 60 * 24)
    dd = seconds % (365 * 60 * 60 * 24)
    d = dd // (60 * 60 * 24)
    hh = seconds % (60 * 60 * 24)
    h = hh // (60 * 60)
    mm = seconds % (60 * 60)
    m = mm // 60
    s = mm % 60

    print(y, d, hh, h, mm, m, s)

    if y == 0 :
        y = ""
        flag = 0
    else : 
        y =  str(y) + " year" + ( "s" if y > 1 else "" )
        flag = 1

    if d == 0 :
        d = ""
        flag = 0
    else : 
        d =  ( ", " if(flag) else "") + str(d) + " day" + ( "s" if d > 1 else "" )
        flag = 1

    if h == 0 :
        h = ""
        flag = 0
    else : 
        h =  ( ", " if(flag) else "") + str(h) + " hour" + ( "s" if h > 1 else "" )
        flag = 1

    if m == 0 :
        m = ""
        flag = 0
    else : 
        if s==0:
            x = " and "
        else:
           x = ", "
        m =  (x if(flag) else "") + str(m) + " minute" + ( "s" if m > 1 else "" )
        flag = 1

    if s == 0 :
        s = ""
    else : 
        s = ( " and " if(flag) else "") + str(s) + " second" + ( "s" if s > 1 else "" )

    return y + d + h + m + s



from unittest import TestCase 

test = TestCase()

try:
    test.assertEquals(format_duration(1), "1 second")
    test.assertEquals(format_duration(62), "1 minute and 2 seconds")
    test.assertEquals(format_duration(120), "2 minutes")
    test.assertEquals(format_duration(3600), "1 hour")
    test.assertEquals(format_duration(3662), "1 hour, 1 minute and 2 seconds")
    test.assertEquals(format_duration(15731080), "'182 days, 1 hour, 44 minutes and 40 seconds'")

except Exception as e:
    print(e)
