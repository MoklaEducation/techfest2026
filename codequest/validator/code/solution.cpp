#include <bits/stdc++.h>
using namespace std;
bool valid(const string& s){
    vector<string> parts;
    stringstream ss(s);
    string tok;
    while(getline(ss,tok,'.')) parts.push_back(tok);
    if(parts.size()!=4) return false;
    for(auto& g:parts){
        if(g.empty()||!all_of(g.begin(),g.end(),::isdigit)) return false;
        if(g.size()>1&&g[0]=='0') return false;
        if(stoi(g)>255) return false;
    }
    return true;
}
int main(){
    ios::sync_with_stdio(false);cin.tie(nullptr);
    int t;cin>>t;cin.ignore();
    while(t--){
        string s;getline(cin,s);
        cout<<(valid(s)?"VALID":"INVALID")<<"\n";
    }
}