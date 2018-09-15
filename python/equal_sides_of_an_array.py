def find_even_index(arr):
    print(arr)
    #your code here
    left_sum = 0
    right_sum = 0
    
    for ix, i in enumerate(arr):
        left_sum = sum(arr[:ix])
        right_sum = sum(arr[ix+1:])

        print("ix, i, left_sum, right_sum: ", ix, i, left_sum, right_sum)
        if left_sum == right_sum :
            return ix



            
    return -1



        
        
# find_even_index([1,2,3,4,3,2,1])
print(find_even_index([-1, -2, -3, -4, -3, -2, -1]))
