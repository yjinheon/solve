#include <iostream>
#include <vector>
using namespace std;

// fibo(N)의 답을 담는 vector

// 0 1 1 2 3 5 8
// 0 1 2 3 4 5 6

vector<long long> memo;

long long fibo_memo(int N) {

  // base case

  if (N == 0)
    return 0;
  else if (N == 1)
    return 1;

  // if cached return cached value
  if (memo[N] != -1)
    return memo[N];

  return memo[N] = fibo_memo(N - 1) + fibo_memo(N - 2);
}

int main() {
  memo.assign(50, -1); // -1 * 50으로 초기화

  // call fibo_memo 49

  fibo_memo(49);

  for (int N = 2; N < 50; ++N) {

    cout << N << " 항째 : " << memo[N] << endl;
  }
}
