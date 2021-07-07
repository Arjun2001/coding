class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        prime = [1] * n
        i = 2
        while (i*i < n):
            if prime[i] == 1:
                for j in range(i*i,n,i):
                    prime[j] = 0
            i += 1
        total = 0
        for i in range(2,n):
            if prime[i] == 1:
                total += 1
        return total