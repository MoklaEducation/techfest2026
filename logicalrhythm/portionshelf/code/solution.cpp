#include <bits/stdc++.h>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        int mx = *max_element(a.begin(), a.end());
        int second = INT_MIN; bool found = false;
        for (int v : a) if (v < mx) { second = max(second, v); found = true; }
        if (found) cout << second << "\n";
        else cout << "NO BACKUP\n";
    }
}