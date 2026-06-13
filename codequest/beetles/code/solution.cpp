#include <bits/stdc++.h>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        unordered_set<int> seen;
        vector<int> order;
        for (int i = 0; i < n; i++) {
            int x; cin >> x;
            if (!seen.count(x)) { seen.insert(x); order.push_back(x); }
        }
        cout << "Count: " << order.size() << "\n";
        for (int i = 0; i < (int)order.size(); i++) {
            if (i) cout << ' ';
            cout << order[i];
        }
        cout << "\n";
    }
}