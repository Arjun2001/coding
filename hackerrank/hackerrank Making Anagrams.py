import sys

def solve(s1,s2,mp):
    ans = {}
    for i in s1:
        if i not in ans:
            ans[i] = 0
        ans[i] += 1
    for i in s2:
        if i not in ans:
            ans[i] = 0
        ans[i] -= 1
    tot = 0
    for i in ans:
        tot += abs(ans[i])
    return tot

s1 = "absdjkvuahdakejfnfauhdsaavasdlkj"
s2 = "djfladfhiawasdkjvalskufhafablsdkashlahdfa"
mp = {}
print(solve(s1,s2,mp))