#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int t; cin>>t;
    while(t--){
        int n,k; cin>>n>>k;
        vector<int> a(n);
        for(auto& x:a) cin>>x;
        deque<int> dq;
        for(int i=0;i<n;i++){
            while(!dq.empty()&&dq.front()<i-k+1) dq.pop_front();
            while(!dq.empty()&&a[dq.back()]<=a[i]) dq.pop_back();
            dq.push_back(i);
            if(i>=k-1){
                if(i>k-1) cout<<' ';
                cout<<a[dq.front()];
            }
        }
        cout<<'\n';
    }
}