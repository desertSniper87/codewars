#include "string-repeat.c"
#include <stdio.h>

int main () {
    size_t count = 9;

    /*const char *str = "a";*/
    /*char *result = repeat_str(count, str);*/

    /*const char *str = "hello ";*/
    /*char *result = repeat_str(count, str);*/

    /*const char *str = "*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&";*/
    /*char *result = repeat_str(count, str);*/

    const char *str = "mpGNKC5IO1dIGy0NlLA(oWR1dKtW(jKU";
    char *result = repeat_str(count, str);

    printf("%s\n", result);

    return 0;

}
