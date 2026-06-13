#include <bits/stdc++.h>
using namespace std;
int main() {
    int t; cin >> t; cin.ignore();
    while (t--) {
        string s; getline(cin, s);
        stack<char> stk;
        bool ok = true;
        for (char c : s) {
            if (c=='(' || c=='[' || c=='{') { stk.push(c); continue; }
            if (c==')' || c==']' || c=='}') {
                if (stk.empty()) { ok=false; break; }
                char top = stk.top(); stk.pop();
                if ((c==')' && top!='(') || (c==']' && top!='[') || (c=='}' && top!='{'))
                { ok=false; break; }
            }
        }
        cout << ((ok && stk.empty()) ? "SAFE" : "DANGEROUS") << "\n";
    }
}