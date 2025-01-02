#include <iostream>
#include <vector>

using namespace std;

int main() {

  // input
  int N, v;
  cin >> N >> v;
  vector<int> a(N);
  for (int i = 0; i < N; ++i)
    cin >> a[i];

  // linear search
  int found_id = -1;
  for (int i; i < N; ++i) {
    if (a[i] == v) {
      found_id = i;
    }
  }

  // print

  cout << found_id << endl;
}
