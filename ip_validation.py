def is_valid_IP(strng):
    print(strng)
    a = strng.split('.')
    if strng=='' or len(a)!=4:
        return False
    # print(a)
    for i in a:
        # print("i, i[0], len(i)", i, i[0], len(i))
        if len(i)==3 and i[0]=='0':
            return False
        if not (i.isdigit()==True and int(i)>=0 and int(i)<=255):
            return False
            # print(i)

    print('True')
    return True

if __name__ == "__main__":
    is_valid_IP('12.255.56.1')    
    is_valid_IP('')               
    is_valid_IP('abc.def.ghi.jkl')
    is_valid_IP('123.456.789.0')  
    is_valid_IP('12.34.56')       
    is_valid_IP('12.34.56 .1')    
    is_valid_IP('12.34.56.-1')    
    is_valid_IP('123.045.067.089')
    is_valid_IP('127.1.1.0')      
    is_valid_IP('0.0.0.0')        
    is_valid_IP('0.34.82.53')     
    is_valid_IP('192.168.1.300')  
