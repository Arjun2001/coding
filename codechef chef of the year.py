c,n = list(map(int,input().split()))
country= dict()
country_mem = dict()
count = dict()
for i in range(c):
    temp = list(input().split())
    country[temp[1]] = 0
    country_mem[temp[0]] = temp[1]
    count[temp[0]] = 0
for i in range(n):
    temp = input()
    count[temp] += 1
    country[country_mem[temp]] += 1
maxi = 0
for i in sorted(country):
    if country[i]>maxi:
        maxi = country[i]
        ans = i
print(ans)
maxi = 0
for i in sorted(count):
    if count[i]>maxi:
        maxi = count[i]
        ans = i
print(ans)
