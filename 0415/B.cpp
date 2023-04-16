#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

void solve(int n, int q, vector<vector<int>>& queries) {
    vector<vector<int>> cards(n+1);
    vector<vector<int>> nums(2*100000+1);

    for (int i = 0; i < q; i++) {
        int query_type = queries[i][0];
        if (query_type == 1) {
            int x = queries[i][1];
            int y = queries[i][2];
            cards[y].push_back(x);
            nums[x].push_back(y);
        } else if (query_type == 2) {
            int x = queries[i][1];
            vector<int> sorted_cards(cards[x].begin(), cards[x].end());
            sort(sorted_cards.begin(), sorted_cards.end());
            for (int j = 0; j < sorted_cards.size(); j++) {
                cout << sorted_cards[j] << " ";
            }
            cout << endl;
        } else if (query_type == 3) {
            int x = queries[i][1];
            set<int> sorted_nums(nums[x].begin(), nums[x].end());
            for (auto it = sorted_nums.begin(); it != sorted_nums.end(); it++) {
                cout << *it << " ";
            }
            cout << endl;
        }
    }
}

int main() {
    int n, q;
    cin >> n >> q;
    vector<vector<int>> queries(q, vector<int>(3));
    for (int i = 0; i < q; i++) {
        cin >> queries[i][0] >> queries[i][1];
        if (queries[i][0] == 1) {
            cin >> queries[i][2];
        }
    }

    solve(n, q, queries);

    return 0;
}