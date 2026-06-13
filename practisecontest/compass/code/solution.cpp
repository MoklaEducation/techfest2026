#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int T; cin >> T;
    string s;
    while(T--){
        cin >> s;
        int x=0,y=0;
        for(char c: s){
            if(c=='E') x++; else if(c=='W') x--; else if(c=='N') y++; else if(c=='S') y--;
        }
        cout << "Position = (" << x << ", " << y << "), Distance = " << abs(x)+abs(y);
        if(T) cout << '\n';
    }
    return 0;
}
