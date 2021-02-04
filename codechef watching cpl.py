import sys
def findMin(a, n):
     
    su = 0
    su = sum(a)
    
    dp = [[0 for i in range(su + 1)] 
             for j in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True
         
    for j in range(1, su + 1):
        dp[0][j] = False
     
    for i in range(1, n + 1):
        for j in range(1, su + 1):
            dp[i][j] = dp[i - 1][j]
            if a[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - a[i - 1]]
    diff = sys.maxsize
    for j in range(su // 2, -1, -1):
        if dp[n][j] == True:
            diff = su - (2 * j)
            break
             ;
    return diff

for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    tot_sum = 2*k
    sum1 = 0
    flag = 0
    for i in range(n):
        sum1 += a[i]
        if sum1 >= tot_sum and flag == 0:
            split_arr = a[:i+1]
            if i==0 :
                continue
            diff = findMin(split_arr,i+1)
            if sum1-tot_sum >= diff:
                print(i+1)
                flag = 1
                break
            else:
                need = diff - (sum1-tot_sum)
                flag = 2
        elif flag == 2:
            if a[i] > need or need <= 0:
                print(i+1)
                flag = 1
                break
            else:
                need -= a[i]
    if flag != 1:
        print('-1')


                
        



            
