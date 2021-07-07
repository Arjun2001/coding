a = []
for _ in range(int(input())):
    a.append(int(input()))

l = len(a)
left = [0]*l
right = [0]*l
left[0] = a[0]
right[l-1] = a[l-1]

for i in range(1, l):
    left[i] = max(left[i-1], a[i])

for i in range(l-2,-1,-1):
    right[i] = max(right[i+1], a[i])

ans = 0
for i in range(l):
    ans += min(left[i], right[i]) - a[i]

print(ans)

