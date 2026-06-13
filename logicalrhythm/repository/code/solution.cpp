#include <bits/stdc++.h>
using namespace std;
int main() {
    int q; cin >> q;
    while (q--) {
        int n, t; cin >> n >> t;
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        int lo = 0, hi = n - 1, result = -1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (a[mid] == t)     { result = mid; break; }
            else if (a[mid] < t) lo = mid + 1;
            else                 hi = mid - 1;
        }
        cout << result << "\n";
    }
}