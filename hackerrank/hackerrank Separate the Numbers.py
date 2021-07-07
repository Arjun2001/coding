def generate(s,l):
    temp = int(s)
    temps = s
    while(len(temps) < l):
        temps += str(temp+1)
        temp += 1
    return temps
s = "99100"
l = len(s)
temp = ""
for i in range(l):
    temp += s[i]
    if generate(temp,l) == s and i != l-1:
        print("YES",temp)
        break
print("NO")
    