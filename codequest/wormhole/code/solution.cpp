#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false);cin.tie(nullptr);
    int t;cin>>t;
    while(t--){
        int n,k;cin>>n>>k;
        vector<int> a(n);
        for(auto& x:a)cin>>x;
        sort(a.begin(),a.end());
        cout<<a[k-1]<<' '<<a[(n-1)/2]<<"\n";
    }
}