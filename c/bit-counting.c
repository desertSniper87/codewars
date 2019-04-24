#include <stddef.h>
#include <stdio.h>

size_t countBits(unsigned value){
    int bits = 0;

    for (int i=16; i>=0; i--) {
        int k = value >> i;

        if (k & i){
            bits += 1;
        }
    }

    printf("%d\n", bits);

    return bits;

}
