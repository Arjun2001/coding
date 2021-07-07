#include <bits/stdc++.h>
using namespace std;

#define long long int ll

void fast() { ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);}

int main() {
    fast();
    ll tc;
    cin>>tc;
    while(tc--) {
        ll n,x;
        cin>>n>>x;
        map<int,int> m;
        ll temp;
        for (int i=0;i<n;i++){
            cin>>temp;
            if (m.find(temp) == m.end()) {
                m[temp] = 1;
            }
        }
        cout<<len(m)<<endl;
    }
}
