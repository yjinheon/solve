#include <iostream>
#include <vector>

using namespace std;

const int INF = 200000;

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  for (int i = 0; i < n; i++)
    cin >> a[i];

  int min_value = INF;
  for (int i = 0; i < n; i++) {
    if (a[i] < min_value) {
      min_value = a[i];
    }
  }

  cout << min_value << endl;
}
