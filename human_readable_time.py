def make_readable(seconds):
    """TODO: Docstring for make_readable.

    :seconds: INT
    :returns: string, time

    """
    h = 0
    m = 0
    s = 0
    m += seconds/60
    s += seconds%60
    h =  m/60
    m = m%60
    # print(h, m, s)
    return str("%02d"%h)+':'+str("%02d"%m)+':'+str("%02d"%s)

def make_readable_2(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

if __name__ == "__main__":
    x = make_readable(86399)
    # x = make_readable(0)
    print(x)
