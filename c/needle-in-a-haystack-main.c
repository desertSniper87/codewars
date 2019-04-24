#include <stdio.h>
#include "needle-in-a-haystack.c"

int main(int argc, char *argv[])
{   const char *haystack[] = { "3", "123124234", "None", "needle", "world", "hay", "2", "3" };
    printf("%s\n", find_needle(haystack, sizeof(haystack)/sizeof(haystack[0])));

    return 0;
}
