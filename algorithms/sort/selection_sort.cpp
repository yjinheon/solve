// 크기 n의 배열이 주어졌을 때 index 0부터 n-1까지의 모든 index i 에 대해
// i 부터 n-1까지의 값 중 가장 작은 값을 구해 index i에 둔다.n-1까지의

#include <stdio.h>

int main(void) {
  int i, j, min, idx, tmp;
  int array[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
  for (i = 0; i < 10; i++) {
    min = 9999;
    for (j = i; j < 10; j++) {
      if (min > array[j]) {
        min = array[j];
        idx = j;
      }
    }
  }
  tmp = array[i];
  array[i] = array[idx];
  array[idx] = tmp;

  for (i = 0; i < 10; i++) {
    printf("%d", array[i]);
  }

  return 0;
}
