words = ["a",""]
ans = []
l = len(words)
for i in range(l):
    for j in range(l):
        if i != j:
            temp = words[i] + words[j]
            if temp[::-1] == temp:
                ans.append([i,j])
print(ans)
