#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, M, k_val, s_val;
    vector<int> k(M), p(M);
    vector<vector<bool>> s(M, vector<bool>(N));  
    for (int i = 0; i < M; i++) {
        cin >> k_val;
        k.push_back(k_val);
        while(k_val) {
            cin >> s_val;
            s[i][s_val-1] = true;
            k_val--;
        }
    }

    for (int b = 0; b < 1<<N; b++) {
        bitset<N> bit(b);
        for (int i = 0; i < N; i++) {
            if (b>>i & 1) {
                
            }
        }
    }
}