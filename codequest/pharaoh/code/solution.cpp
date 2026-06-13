#include <bits/stdc++.h>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        int maxVal = INT_MIN;
        for (int i = 0; i < n; i++) {
            int v; cin >> v;
            maxVal = max(maxVal, v);
        }
        cout << maxVal << "\n";
    }
}