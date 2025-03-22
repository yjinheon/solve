// subarray

#include <iostream>
#include <vector>

using namespace std;

int main() {
    // input
    int N ,M;

    cin >> N >>M;
    vector<int> a(N);

    for (int i =0; i<N ; ++i) cin >> a[i];

    bool exist = false;

    // bit full search 2^N
    for (int bit = 0; bit < (1 << N); ++bit) {
        vector<int> S;
        for (int i = 0; i < N; ++i) {
            if (bit & (1 << i)) {
                S.push_back(a[i]);
            }
        }

        // check if the sum of the subarray is M
        int sum = 0;
        for (int i = 0; i < S.size(); ++i) {
            sum += S[i];
        }

        if (sum == M) {
            exist = true;
        }
    }

}