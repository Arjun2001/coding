n1, n2, n3 = map(int, input().split())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s3 = list(map(int, input().split()))

s1 = s1[::-1]
s2 = s2[::-1]
s3 = s3[::-1]

sum1 = sum(s1)
sum2 = sum(s2)
sum3 = sum(s3)

min_ht = min(sum1, sum2, sum3)
while(sum1 != sum2 or sum1 != sum3):
    while(sum1 > min_ht):
        sum1 -= s1.pop()
    min_ht=min(sum1,sum2,sum3)
    while(sum2>min_ht):
        sum2 -= s2.pop()
    min_ht = min(sum1,sum2,sum3)
    while(sum3 > min_ht):
        sum3 -= s3.pop()
    min_ht = min(sum1,sum2,sum3)
print(min_ht)