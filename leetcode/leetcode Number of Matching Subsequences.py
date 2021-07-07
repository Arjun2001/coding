import bisect
from collections import defaultdict
s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]

mp = defaultdict(list)
for i in range(len(s)):
    mp[s[i]].append(i)
ans = 0
for word in words:
    found = True
    prev = -1
    for c in word:
        pos = bisect.bisect(mp[c],prev)
        if pos == len(mp[c]):
            found = False
            break
        else:
            prev = mp[c][pos]
    ans += found == True
print(ans)
