// 쌍의 합이 K 이상인 값 중 최소

#include <iostream>
#include <vector>

using namespace std;

const int INF = 2000000;

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> a(n), b(n); // initialize 2 vector with length n
  for (int i = 0; i < n; ++i) {
    cin >> a[i];
  }
  for (int i = 0; i < n; ++i) {
    cin >> b[i];
  }

  int min_val = INF;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (a[i] + b[j] < k)
        continue;
      if (a[i] + b[j] < min_val) {
        min_val = a[i] + b[j];
      }
    }
  }

  cout << min_val << endl;
}
