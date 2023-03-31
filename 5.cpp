#include <bits/stdc++.h>
using namespace std;


int main() {
    int A, B, C, X, Y;
    cin >> A >> B >> C >> X >> Y;
    int all_num = 2 * max(X, Y);
    int price = INT_MAX;
    for (int C_num = 0; C_num < all_num+1; C_num++) {
        int A_num = max(0, X - C_num/2);
        int B_num = max(0, Y - C_num/2);
        int tmp_price = A*A_num + B*B_num + C*C_num;
        if (price > tmp_price) {
            price = tmp_price;
        }
    }
    cout << price << endl;
}
