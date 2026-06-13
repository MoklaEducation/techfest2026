#include <bits/stdc++.h>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        long long total = 0;
        for (int i = 0; i < n; i++) { int x; cin >> x; total += x; }
        cout << "Total: " << total << "\n";
        cout << "Average: " << total / n << "\n";
    }
}