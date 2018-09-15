#include <stdio.h>
#include <math.h>

int nbDig(int n, int d) {
  // your code
  int i, x;
  int digits_in_x;
  int j;
  int max = 0;
  if (d==0) {
      max ++;
  }

  for (i=1; i<=n; i++) {
      x = i*i;
      digits_in_x = log10(x) + 1;
      
      for (j=0; j<digits_in_x; j++, x/=10) {
          if (x%10 == d) {
              max++;
          }
      }


  }

  return max;
}

