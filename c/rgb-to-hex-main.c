#include <stdio.h>
#include "rgb-to-hex.c"

int main() {
    
    char x[20];
    rgb(255, 255, 255, x);
    printf("%s\n", x);

    rgb(148, 1, 211, x);
    printf("%s\n", x);
    
    return 0;
}
