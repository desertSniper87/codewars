#include <string.h>
#include <stdlib.h>
#include <stdio.h>

char *repeat_str(size_t count, const char *src) {
  printf("count: %d src: %s\n", (int) count, src);
  int i, j;
  /*int src_ptr_l = sizeof(src);*/
  int src_l = strlen(src);
  char* ret = (char*) malloc( sizeof(char) * (count * src_l));

  for (i=0;i<(int)(count);i++) {
      for (j=0;j<(int) src_l;j++) {
          ret[(i * src_l)+j] = *(src + j);
      }
  }

  ret[(count * src_l)] = '\0';

  return ret;
}
