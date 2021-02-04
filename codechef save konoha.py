from heapq import heapify,heappop,heappush
def killer(n,a,k):
    heap = [-1*i for i in a]
    heapify(heap)
    count = 0
    while(k>0):
        temp = -1 * heappop(heap)
        if temp == 0:
            return 'Evacuate'
        else:
            k -= temp
            temp = temp//2
            heappush(heap, -1 * temp)
            count += 1
    return count



test = int(input())
while(test):
    test -= 1
    n,k = list(map(int,input().split()))
    a =list(map(int,input().split()))
    print(killer(n,a,k))
