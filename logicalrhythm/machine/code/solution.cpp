#include <bits/stdc++.h>
using namespace std;
int main() {
    int t; cin >> t; cin.ignore();
    while (t--) {
        int n; cin >> n; cin.ignore();
        queue<string> vip, normal;
        for (int i = 0; i < n; i++) {
            string name, type; cin >> name >> type; cin.ignore();
            if (type == "VIP") vip.push(name);
            else normal.push(name);
        }
        while (!vip.empty())    { cout << vip.front()    << "\n"; vip.pop(); }
        while (!normal.empty()) { cout << normal.front() << "\n"; normal.pop(); }
    }
}