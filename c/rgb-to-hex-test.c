#include <criterion/criterion.h>
#include "rgb-to-hex.c"

int rgb(int r, int g, int b, char *output);

Test(RGBToHexConversion, BasicTests) 
{
  int r[] = {0, 1, 255, 254, -20};
  int g[] = {0, 2, 255, 253, 275};
  int b[] = {0, 3, 255, 252, 125};
  
  unsigned int input_sz = sizeof(r)/sizeof(int);
  
  char output[input_sz][7];
  
  char *expected[] = {"000000", "010203", "FFFFFF", "FEFDFC", "00FF7D"};
  for(int i = 0; i < input_sz; i++)
  {
     rgb(r[i], g[i], b[i], output[i]);
     cr_assert_eq(strcmp(output[i],expected[i]), 0,"Error: \nGot: %s\nExpected: %s",output[i],expected[i]);
  }

}


