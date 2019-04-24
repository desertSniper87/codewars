#include <stddef.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

char *find_needle(const char **haystack, size_t count){
    int find;
    size_t i;

    for (i=0; i<count ; i++) {
        if (!strcmp(haystack[i], "needle")){
            find = i;
            break;
        }
    }

    /*char *ret_string =  "found the needle at position ";*/
    char *ret_string = (char*) malloc(sizeof(char) * 64);

    sprintf(ret_string, "found the needle at position %d", find);

    return ret_string;

}
