
#include <iostream>
using namespace std;

int main() {
  int bit = 5;                  // 5 = 0b0101
  for (int i = 0; i < 4; i++) { // 0부터 3번째 비트를 확인
    if (bit & (1 << i)) {
      cout << "Bit " << i << " is 1" << endl;
    } else {
      cout << "Bit " << i << " is 0" << endl;
    }
  }
  return 0;
}
