mod = (10**9)+7

for _ in range(int(input())):
    st = input()
    l = len(st)
    dp = [[-1 for x in range(l+2)] for y in range(l+2)]
    mp = {}
    ans = 0
    for i in range(0,l):
        subs = ''
        for j in range(i,l):
            subs = "".join((subs+st[j]))
            if subs not in mp:
                mp[subs] = ((j-i+1)**len(set(subs)))%mod
                ans += mp[subs]
    print(ans%mod)