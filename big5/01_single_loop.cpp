#include <iostream>
using namespace std;

int main() {

  int n;
  cin >> n;

  int cnt = 0;

  for (int i = 0; i < n; ++i) {
    ++cnt;
    cout << "number : " << i << endl;
  }

  cout << "toal number : " << cnt << endl;
}
