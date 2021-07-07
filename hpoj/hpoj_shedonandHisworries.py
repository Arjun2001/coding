import sys

def printfn(val):
    print(val)
    
def createArr(m):
    arr = []
    for i in range(m):
        temp = list(map(int,input().split()))
        arr.append(temp)
    return arr

def minCost(arr,m,n):
    if (n < 0 or m < 0):
        return sys.maxsize
    elif(m == 0 and n == 0):
        return arr[m][n]
    else:
        return arr[m][n] + min(minCost(arr,m-1,n),minCost(arr,m,n-1))


m , n = map(int,input().split())
arr = createArr(m)
result = minCost(arr,m-1,n-1)
printfn(result)