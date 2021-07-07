arr = [1,2,3,4,5,6,7,8,9,10]
freq = {}
for i in arr:
    if i not in freq:
        freq[i] = 0
    freq[i] += 1

freq = dict(sorted(freq.items(),reverse=True,key = lambda x: x[1]))
half = len(arr)//2
set_size = found = 0
for i,j in enumerate(freq):
    set_size += freq[j]
    if set_size >= half:
        break
print(i+1)