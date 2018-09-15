#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int rgb(int r, int g, int b, char *output)
{
    if (r<0) r = 0;
    if (g<0) g = 0;
    if (b<0) b = 0;

    if (r>255) r = 255;
    if (g>255) g = 255;
    if (b>255) b = 255;

    char hex_r[10];
    char hex_g[10];
    char hex_b[10];

    sprintf(&hex_r, "%02x", r);
    sprintf(&hex_g, "%02x", g);
    sprintf(&hex_b, "%02x", b);

    char * c = hex_r;
    while(*c) {
        *c = toupper((unsigned char) *c);
        c++;
    }

    c = hex_g;
    while(*c) {
        *c = toupper((unsigned char) *c);
        c++;
    }

    c = hex_b;
    while(*c) {
        *c = toupper((unsigned char) *c);
        c++;
    }

    printf("%s %s %s\n", hex_r, hex_g, hex_b);

    char* hex_code = output;
    strcpy(hex_code, hex_r);
    strcat(hex_code, hex_g);
    strcat(hex_code, hex_b);

    //pass the result to the 'char *output'
    output = hex_code;
    printf("%s\n", output);
    return 0; 
}
