import math

def combination(n):
    return (n*(n-1))//2

def sums(n):
    return (n*(n+1))//2

test=int(input())
while(test):
    test-=1
    n=int(input())
    tot_sum=sums(n)
    if tot_sum%2==0:
        mid_sum=tot_sum//2
        point=int((-1+(math.sqrt(1+(4*tot_sum))))//2)
        point_sum=sums(point)
        if point_sum==mid_sum:
            left_count=point
            right_count=n-point
            print(combination(left_count)+combination(right_count)+right_count)
        elif point_sum<mid_sum:
            count=n-point
            print(count)
        else:
            count=n-point-1
            print(count)
    else:
        print(0)
        
