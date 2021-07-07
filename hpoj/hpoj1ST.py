tc = int(input())
for _ in range(tc):
    no, tr = input().split()
    tr = tr.strip()
    stack = []
    i = 0
    sumof = {}
    curent_sum = 0
    leng = len(tr)
    while(i < leng):
        if(tr[i] == ')'):
            if(tr[i-1] != '('):
                while(stack[-1] != '('):
                    curent_sum -= stack.pop()
                stack.pop()
            else:
                if(i+2 < leng and tr[i+2] == ')' and tr[i+1] == '('):
                    sumof[curent_sum] = 1
                    stack.pop()
                    i += 2
                else:
                    while(stack[-1] != '('):
                        curent_sum -= stack.pop()
                    stack.pop()
        elif(tr[i] == '('):
            stack.append(tr[i])
        else:
            num = []
            while(tr[i] != ')' and tr[i] != '('):
                num.append(tr[i])
                i += 1
            i-=1
            num = int(''.join(num))
            stack.append(num)
            curent_sum += num
        i += 1
    if(sumof.get(int(no),0)):
        print('yes')
    else:
        print('no')