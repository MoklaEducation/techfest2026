#include <bits/stdc++.h>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        vector<int> a(n);
        for (int i = 0; i < n; i++) cin >> a[i];
        vector<long long> pre(n+1,0), suf(n+1,0);
        for (int i = 0; i < n; i++) pre[i+1] = pre[i] + a[i];
        for (int i = 0; i < n; i++) suf[i+1] = suf[i] + a[n-1-i];
        long long best = LLONG_MIN;
        for (int left = 0; left <= k; left++)
            best = max(best, pre[left] + suf[k-left]);
        cout << best << "\n";
    }
}