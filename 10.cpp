#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, q;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }
    cin >> q;
    vector<int> m(q);
    for (int i = 0; i < q; i++) {
        cin >> m[i];
    }
    vector<int> ans_arr;
    for (int b = 0; b < 1 << n; b++) {
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if ((b >> i) & 1) {
                ans += A[i];
            }
        }
        ans_arr.push_back(ans);
    }

    for (int i = 0; i < q; i++) {
        string ans = "no";
        for (int j = 0; j < ans_arr.size(); j++) {
            if (m[i] == ans_arr[j]) {
                ans = "yes";
                break;
            }
        }
        cout << ans << endl;
    }
}