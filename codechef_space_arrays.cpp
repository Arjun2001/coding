#include<bits/stdc++.h>
using namespace std;
#define ll long long int

void fast() { ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL); }

int main() {
    fast();
    ll tc;
    cin>>tc;
    while(tc--) {
        ll n;
        cin>>n;
        ll a[n+1];
        a[0] = 0;
        for (int i=1; i<=n; i++) {
            cin>>a[i];
        }
        sort(a,a+n+1c);
        ll sum = 0 , flag = 0;
        for (int i=1;i<=n;i++) {
            if (a[i] > i) {
                flag = 1;
                break;
            }
            sum += abs(a[i]-i);
        }
        if (flag == 1) cout<<"Second"<<endl;
        else if (sum%2==0) cout<<"Second"<<endl;
        else cout<<"First"<<endl;
    }
}