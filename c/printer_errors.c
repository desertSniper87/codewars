/**
 * Author            : desertsniper87 <torshobuet@gmail.com>
 * Date              : 29.01.2018
 * Last Modified Date: 29.01.2018
 */
#include <stdio.h>

char* printerError(char *s) {
    char y[] = "aaabbbbhaijjjm";
    for (int i=0, j=0; s[i]!='\0'|| y[j]!='\0'; ++i, ++j) {
        printf("%c", s[i]);
    }
    return s;
    // your code
}

int main(){
    /*printf("Hello");*/
    /*char x[1000] = "HELLLO";*/
    char x[] = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz";
    /*char x = "hello";*/
    printerError(x);

    return 0;
}
