#include <stdbool.h>
#include <stdio.h>
#include <string.h>

bool xo (const char* str)
{
    int num_x = 0;
    int num_y = 0;

    for (int i = 0; i < (int) strlen(str) ; ++i) {
        printf("%d %c\n", i, str[i]);
        if (str[i] == 'x' || str[i] == 'X') 
            num_x++;
        else if (str[i] == 'o' || str[i] == 'O')
            num_y++;
    }

    if (num_x==num_y)
        return true;
    printf("%d %d\n", num_x, num_y);

    return false;
}
