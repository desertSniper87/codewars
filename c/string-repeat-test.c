/* Adapted from the tests originally written by a code warrior wichu */

#include <criterion/criterion.h>
#include <string.h>
#include "string-repeat.c"

char *repeat_str(size_t count, const char *src);

Test(ExampleTests, ShouldPassAllTheTestsProvided) {
  {
    size_t count = 4;
    const char *str = "a";
    char *result = repeat_str(count, str);
    cr_assert(strcmp(result, "aaaa") == 0);
    free(result);
  }
  
  {
    size_t count = 3;
    const char *str = "hello ";
    char *result = repeat_str(count, str);
    cr_assert(strcmp(result, "hello hello hello ") == 0);
    free(result);
  }
  
  {
    size_t count = 2;
    const char *str = "abc";
    char *result = repeat_str(count, str);
    cr_assert(strcmp(result, "abcabc") == 0);
    free(result);
  }

  {
    size_t count = 34;
    const char *str = "*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&";
    char *result = repeat_str(count, str);
    cr_assert(strcmp(result, "*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&*a%%Dv6&8(c&lJpV8HCgCicWjdHJ#$8!*a%%Dv6&") == 0);
    free(result);
  }
  {
    size_t count = 9;
    const char *str = "mpGNKC5IO1dIGy0NlLA(oWR1dKtW(jKU";
    char *result = repeat_str(count, str);
    printf("%s\n", result);
    cr_assert(strcmp(result, "mpGNKC5IO1dIGy0NlLA(oWR1dKtW(jKUmpGNKC5IO1dIGy0NlLA(oWR1dKtW(jKUmpGNKC5IO1dIGy0NlLA(oWR1dKtW(jKUmpGNKC5IO1dIGy0NlLA(oWR1dKtW(jKUmpGNKC5IO1dIGy0NlLA(oWR1dKtW(jKUmpGNKC5IO1dIGy0NlLA(oWR1dKtW(jKUmpGNKC5IO1dIGy0NlLA(oWR1dKtW(jKUmpGNKC5IO1dIGy0NlLA(oWR1dKtW(jKUmpGNKC5IO1dIGy0NlLA(oWR1dKtW(jKU") == 0);
    free(result);
  }
}
