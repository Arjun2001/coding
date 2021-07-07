h1,h2,h3 = map(int,input().split())
h1 = list(map(int,input().split()))
h2 = list(map(int,input().split()))
h3 = list(map(int,input().split()))
sums = {}
s1= sum(h1)
s2 = sum(h2)
s3 = sum(h3)
l1 = len(h1)
l2 = len(h2)
l3 = len(h3)
top1 = top2 = top3 = 0
while True:
    if top1 == l1 or top2 == l2 or top3 == l3:
        print(0)
        break
    if s1 == s2 == s3:
        print(s1)
        break
    if s1 >= s2 and s1 >= s3:
        s1 -= h1[top1]
        top1 += 1
    elif s2 >= s1 and s2 >= s3:
        s2 -= h2[top2]
        top2 += 1
    elif s3 >= s1 and s3 >= s1:
        s3 -= h3[top3]
        top3 += 1
