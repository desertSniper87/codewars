#include <stdio.h>

int get_sum(int a , int b) {
    // Good luck
    
    if (a>b) {
        int temp = a;
        a = b;
        b = temp;
    }
    
    int sum = 0;
    for (int i=a+1;i<b;i++){
        sum += i;
    }
    return sum;
}



