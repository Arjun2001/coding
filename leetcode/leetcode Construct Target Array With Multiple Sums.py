import heapq as heap
target = [8,5]
total = sum(target)
target = [-num for num in target]
flag = 0
heap.heapify(target)

while(target[0] != -1):
    temp = heap.heappop(target)
    num = -1 * temp
    total -= num
    if num <= total or total < 1:
        flag = 1
        break
    num %= total
    total += num
    heap.heappush(target,-num or -total)
if flag == 1:
    print('false')
else:
    print('true')