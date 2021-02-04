from sys import stdin, stdout
n,m=map(int,stdin.readline().split())
arr = [[0]*m]*n
temp1=0
while(temp1!=n):
    temp=input()
    for i in range(len(temp)):
        arr[temp1][i]=int(temp[i])
    temp1+=1
q=int(input())
while(q):
    a,b,c,d=map(int,stdin.readline().split())
    print(arr)
    for i in range(a-1,c):
        for j in range(b-1,d):
            print(i,j)
            print(arr[i][j])
            if arr[i][j]==0:
                print("inside if",arr)
                print("bfe",arr[i][j])
                arr[i][j]=1
                print("fre",arr[i][j])
                print("if",arr)
            else:
                arr[i][j]=0
            print("outside if", arr)
    print(arr)
    q-=1
print(arr)
