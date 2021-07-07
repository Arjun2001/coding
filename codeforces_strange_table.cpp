#include<bits/stdc++.h>
using namespace std;
#define ll long long int

void fast() { ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL); }

int main() {
    ll tc,n,m,x;
    cin>>tc;
    while(tc--) {
        cin>>n>>m>>x;
        ll row=0,column=0;
        column = (x-1)/n;
        row = (x-1)%n;
        ll ans = m*(row)+column+1;
        cout<<ans<<endl;
    }
}