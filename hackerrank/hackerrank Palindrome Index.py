def check(s):
    if s == s[::-1]:
        return True
    else:
        return False

s = "baaegaab"
if check(s):
    print(-1)
else:
    st,en = 0,len(s)-1
    while (st <= en):
        if s[st] != s[en]:
            if check(s[st+1:en+1]):
                print(st)
                break
            elif check(s[st:en]):
                print(en)
                break
        st += 1
        en -= 1
print(-1)
