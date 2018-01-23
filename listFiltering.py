def filter_list(l):
     r = []
     for x in l:
         if (isinstance(x, int)==True):
             r.append(x)
     return r

def his_filter_list(l):
      return [i for i in l if not isinstance(i, str)]


if __name__ == '__main__':
    print(filter_list([1,2,'a','b']))
    
