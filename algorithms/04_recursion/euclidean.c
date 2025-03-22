#include <stdio.h>

int euclidean(int a, int b) {
  if (b == 0) {
    return a;
  }
  return euclidean(b, a % b);
}

int main(void) {
  int a = euclidean(210, 7);
  printf("%d \n", a);

  return 0;
}
