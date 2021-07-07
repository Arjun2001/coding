deadends = ["1000","0100","0010","0001"]
target = "1111"
q = ['0000']
steps = 0
dead = set(deadends)
flag = 0
while len(q) != 0:
    for k in range(len(q)):
        cur = q.pop(0)
        if cur == target:
            print(steps)
            flag = 1
            break
        if cur in dead:
            continue
        for i in range(4):
            val = int(cur[i])
            for j in [-1,1]:
                new = (val + j)%10
                new = cur[:i] + str(new) + cur[i+1:]
                if new not in dead:
                    q.append(new)
        dead.add(cur)
    if flag == 1:
        break
    steps += 1
if flag == 0:
    print("-1")
    

