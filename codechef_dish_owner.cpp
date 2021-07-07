#include<bits/stdc++.h>
using namespace std;

void fast() { ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL); }

vector<int> parent;
void init (int n) {
    parent.resize(n+1);
    for (int i=1; i<=n;i++) {
        parent[i] = i;
    }
    
}

int find(int n) {
    if (parent[n] == n) return n;
    parent[n] = find(parent[n]);
    return parent[n];
}


int main() {
    fast();
    int tc;
    cin>>tc;
    while(tc--) {
        int l;
        cin>>l;
        init(l);
        int weight[l+1];
        for (int i=1;i<=l;i++) {
            cin>>weight[i];
        }
        int q;
        cin>>q;
        while(q--) {
            int a,b,c;
            cin>>a;
            if (a == 0) {
                cin>>b>>c;
                b = find(b);
                c = find(c);
                if (b == c) {
                    cout<<"Invalid query!"<<endl;
                } else if (weight[b] > weight[c]) {
                    parent[c] = b;
                    weight[b] = max(weight[b],weight[c]);
                } else if (weight[b] < weight[c]) {
                    parent[b] = c;
                    weight[c] = max(weight[b],weight[c]);
                }
            } else {  
                cin>>b;
                cout<<find(b)<<endl;
            }
        }
    }
}