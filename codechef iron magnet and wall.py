def calc(k,i,j,s):
    count = 0
    if i > j:
        i ,j = j ,i
    for q in range(i,j):
        if s[q] == ':':
            count += 1
    return (k+1-(j-i)-count)

test = int(input())
while(test):
    test -= 1
    n,k = list(map(int,input().split()))
    s = input()
    metal=[]
    iron = []
    ans_count = 0
    for l in range(n):
        if s[l] == 'M':
            metal.append(l+1)
        if s[l] == 'I':
            iron.append(l+1)
        if len(iron)>=1:
            if len(metal)>=1:
                i = metal[-1]
                if calc(k,i,iron[-1],s) > 0:
                    ans_count += 1
                    metal.pop()
                    iron.pop()
        if s[l] == 'X':
            metal = []
            iron = []
    print(ans_count)
            
