#include <stdio.h>

int main(void) {
  int i, j, min, index,temp;

  int array[10] = {1,10,5,8,7,6,4,3,2,9};


  for(i=0; i<10; i++){
    min = 9999; // initialize
    
    for(j=i; j<10; j++){
      if(min > array[j]){
        min = array[j]; // 최솟값
        index = j; // 최솟값의 인덱스(위치)
      }
    }
    temp = array[i]; // swap 
    array[i] = array[index]; // 
    array[index] = temp;
  }

  for(i=0; i<10; i++){
    printf("%d ", array[i]);
  };

  return 0;
}
