for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    s = [int(x) for x in s]
    q = list(map(int,input().split()))
    arr = []
    temp = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            arr.append(2)
            temp += 2
        else:
            arr.append(1)
            temp += 1
    for i in range(k):
        if (q[i] - 2 >= 0):
            if s[q[i]-2] != s[q[i]-1]:
                arr[q[i]-2] += 1
                temp += 1
            else:
                arr[q[i]-2] -= 1
                temp -= 1
        if (q[i] < n):
            if s[q[i]] != s[q[i]-1]:
                arr[q[i]-1] += 1
                temp += 1
            else:
                arr[q[i]-1] -= 1
                temp -= 1
        if(s[q[i]-1]) == 1:
            s[q[i]-1] = 0
        else:
            s[q[i]-1] = 1
        print(temp)