arr = [1 ,2, 3, 5, 4]
n = len(arr)
inv = 0
for i in range(n):
   for j in range(i+1,n):
        if arr[i] > arr[j]:
            inv += 1
if inv%2 == 0:
    print("YES")
else:
    print("NO")
        