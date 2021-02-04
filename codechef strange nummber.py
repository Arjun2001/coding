import math
def countDivisors(x):
    ctr=0
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i == 0):
            while(x%i == 0):
                ctr+=1
                x=x/i
    return ctr

    
if __name__ == "__main__":
    test=int(input())
while(test):
    x,k=list(map(int,input().split()))
    ctr1=countDivisors(x)
    if(ctr1>=k):
        print(1)
    else:
        print(0)
    test-=1

