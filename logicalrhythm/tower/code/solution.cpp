#include <bits/stdc++.h>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        stack<int> tower;
        vector<int> discard;
        for (int i = 0; i < n; i++) {
            int b; cin >> b;
            if (tower.empty() || b < tower.top()) tower.push(b);
            else discard.push_back(b);
        }
        if (discard.empty()) { cout << "EMPTY DISCARD\n"; continue; }
        for (int i = 0; i < (int)discard.size(); i++) {
            if (i) cout << ' ';
            cout << discard[i];
        }
        cout << "\n";
    }
}