#include <iostream>
using namespace std;

int func(int n) {

  // calling recursive func
  cout << "called func(" << n << ") " << endl;

  if (n == 0)
    return 0;

  int res = n + func(n - 1);
  cout << n << "까지의 합 = " << res << endl;

  return res;
}

int main() { func(5); }
