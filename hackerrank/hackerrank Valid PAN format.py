import re
for _ in range(int(input())):
    s = input()
    if re.search(r'^[A-Z]{5}[0-9]{4}[a-zA-Z]$', s):
        print("YES")
    else:
        print("NO")