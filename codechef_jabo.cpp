#include<bits/stdc++.h>
using namespace std;

void fast() { ios_base::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL); }

vector<int> parent,rank,source;

void init (int n) {
    parent.resize(n+1);
    source.resize(n+1);
    rank.resize(n+1,1);
    for (int i=0; i<=n; i++) {
        parent[i] = i;
    }
}

int find(int n) {
    if (parent[n] == n): return n
    parent[n] = find(parent[n]);
    return parent[n];
}

void join(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b): return
    if (rank[a] >= rank[b]) {
        parent[b] = a;
        rank[a] += rank[b];
        source[a] +=source[b];
    } else {
        parent[a] = b;
        rank[b] += rank[a];
        source[b] += source[a];
    }
}
