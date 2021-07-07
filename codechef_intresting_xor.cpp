#include<bits/stdc++.h>
using namespace std;
#define ll long long int


void fast() { ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL); }
int main() {
    fast();
    ll tc;
    cin>>tc;
    while(tc--) {
        ll c;
        cin>>c;
        ll number = c,i= 0;
        while (number > 0) {
            number = number/2;
            i++;
        }
        ll a = pow(2,i-1)-1;
        ll b = a^c;
        cout<<a*b<<endl;
    }
}