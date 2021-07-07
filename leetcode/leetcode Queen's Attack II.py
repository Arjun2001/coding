n = 4
obstacles = []
mp = {}
for i in obstacles:
    mp[(i[0],i[1])] = 1

r_q, c_q = 4,4
ans = 0

# towards up
i,j = r_q-1,c_q
while (i >= 1 and j >= 1 and i <= n and j <= n):
    if (i,j) in mp:
        break
    else:
        ans += 1
        i -= 1

# towards down
i,j = r_q+1,c_q
while (i >= 1 and j >= 1 and i <= n and j <= n):
    if (i,j) in mp:
        break
    else:
        ans += 1
        i += 1
# towards left
i,j = r_q,c_q-1
while (i >= 1 and j >= 1 and i <= n and j <= n):
    if (i,j) in mp:
        break
    else:
        ans += 1
        j -= 1

# towards right
i,j = r_q,c_q + 1
while (i >= 1 and j >= 1 and i <= n and j <= n):
    if (i,j) in mp:
        break
    else:
        ans += 1
        j += 1

# towards right down diagonal
i,j = r_q+1,c_q+1
while (i >= 1 and j >= 1 and i <= n and j <= n):
    if (i,j) in mp:
        break
    else:
        ans += 1
        i += 1
        j += 1
# towards left up diagonal
i,j = r_q-1,c_q-1
while (i >= 1 and j >= 1 and i <= n and j <= n):
    if (i,j) in mp:
        break
    else:
        ans += 1
        i -= 1
        j -= 1
# towards left down diagoanl
i,j = r_q+1,c_q-1
while (i >= 1 and j >= 1 and i <= n and j <= n):
    if (i,j) in mp:
        break
    else:
        ans += 1
        i += 1
        j -= 1
# towards right up diagonal
i,j = r_q-1,c_q + 1
while (i >= 1 and j >= 1 and i <= n and j <= n):
    if (i,j) in mp:
        break
    else:
        ans += 1
        i -= 1
        j +=  1
print(ans)
