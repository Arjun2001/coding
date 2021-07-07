fact = [1]
mod = 1000000007
for i in range(1, 10**5 + 1):
    fact.append((fact[-1]*i) % mod)

for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    aone = a.count('1')
    bone = b.count('1')
    mini =  abs(aone - bone)
    maxi = (aone + bone) - (2 * max(0, aone + bone - n))
    ans = 0
    for i in range(mini, maxi+1, 2):
        ans = (ans + (fact[n] * pow(fact[i], mod-2, mod) * pow(fact[n-i], mod-2, mod)) % mod) % mod 
    print(ans)