n , m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
mini = a.index(min(a))
maxi = b.index(max(b))
for i in range(m):
    print(mini,i)
for i in range(n):
    if i!= mini:
        print(i,maxi)
        
