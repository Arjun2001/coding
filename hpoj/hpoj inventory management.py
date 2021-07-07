class inventry:
    def __init__(self, arr):
        self.arr = arr
    def invent(self):
        n = len(self.arr)
        ans = [1]
        for i in range(1,n):
            span = 1
            for j in range(i-1, -1, -1):
                if self.arr[i] >= self.arr[j]:
                    span += 1
                else:
                    break
            ans.append(span) 
        return ans

        
arr = []
for i in range(7):
    arr.append(int(input()))
ans = inventry(arr)
ans = ans.invent()
for i in ans:
    print(i)