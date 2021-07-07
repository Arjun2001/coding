#include<bits/stdc++.h>
using namespace std;

void fast() { ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL); }

vector<int> parent;
vector<int> rank1;


void init(int n) {
    parent.resize(n+1);
    rank1.resize(n+1);
    for (int i = 1; i<=n; i++) {
        parent[i] = i;
        rank1[i] = 0;
    }
}

int find(int n) {
    if (parent[n] == n) return n;
    parent[n] = find(parent[n]);
    return parent[n];
}

void join(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return;
    if (rank1[b] > rank1[a]) {
        parent[a] = b;
        rank1[b]++;
    } else {
        parent[b] = a;
        rank1[a]++;
    }
}

int A[100010], C[100010], mi[100010];
int main() {
    fast();
    int n,m;
    cin>>n>>m;
    init(n);
    int s,e;
    for (int i=1; i<=m; i++) {
        cin>>s;
        cin>>e;
        join(s,e);
    }

    for(int i=1; i<=n; i++) {
        cin>>A[i];
    }

    for (int i=1; i<=n; i++) {
        C[i] = 0;
        mi[i] = 10001;
    }

    for (int i=1;i<=n;i++) {
        int root = find(i);
        C[root]++;
        if (A[i] >= 0) mi[root] = min(mi[root], A[i]);
    }

    int x = 10001, maxi = 0,k = 0, f = 0;
    for (int i=1; i<=n; i++) {
        if (C[i] > 0) {
            k++;
            if (mi[i] == 10001) f = 1;
            x = min(x, mi[i]);
            maxi += mi[i];
        }
    }
    if (k == 1) {
        cout<<'0'<<endl;
    }

    if (k > 1) {
        if(f) cout<<-1<<endl;
        else {
            cout<<x*(k-1)+maxi-x<<endl;
        }
    }
    return 0;

}
