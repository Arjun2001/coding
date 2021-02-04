n, q = map(int,input().split())
a = list(map(int,input().split()))
count = 0
s = [0]*n
temp = {}
temp[0] = []
temp[0].append(a[0])
for i in range(1,n):
    if a[i] % a[i-1] != 0:
        count += 1
    if  count not in temp:
        temp[count] = []
    s[i] = count
    temp[count].append(a[i])
for i in range(q):
    qu = list(input().split())
    if qu[0] == 1:
        a[qu[1]-1] = qu[2]
        if (qu[2])<=n:
            if a[qu[2]] % a[qu[2]-1] == 0:
                s[qu[2]-1] = s[qu[2]]
            

    
