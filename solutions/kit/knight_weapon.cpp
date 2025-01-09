#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

class Solution {
public:
  static int get_divisor_count(int num) {
    if (num == 0)
      return 0;

    int count = 0;
    for (int i = 1; i * i <= num; i++) {
      if (i * i == num) {
        count++;
      } else if (num % i == 0) {
        count += 2;
      }
    }

    return count;
  }

  int solution(int num, int limit, int power) {
    vector<int> divisors(num); // initialize a int vector

    // generate divisors vector
    generate(divisors.begin(), divisors.end(),
             [n = 0]() mutable { return get_divisor_count(++n); });

    return accumulate(divisors.begin(), divisors.end(), 0,
                      [limit, power](int sum, int count) {
                        return sum + (count > limit ? power : count);
                      });
  }
};

int main() {
  Solution s;
  int num = 5;
  int limit = 2;
  int power = 3;
  int result = s.solution(num, limit, power);
  cout << "result: " << result << endl;
  return 0;
}
