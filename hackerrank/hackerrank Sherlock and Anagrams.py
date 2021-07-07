s = "kkkk"
mp = {}
for i in range(len(s)):
    subs = ""
    for j in range(i,len(s)):
        subs = "".join(sorted(subs+s[j]))
        if subs not in mp:
            mp[subs] = 0
        mp[subs] += 1
ans = 0
for i,j in mp.items():
    ans += (j*(j-1))//2
print(ans)