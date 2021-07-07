import math,sys

def input(): return sys.stdin.readline().rstrip("\r\n")

def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()

def find_in_pos(x,s):
    l = len(s)
    count = 0
    temp_count= 0
    for j in range(0,x):
        temp_count = 0
        for i in range(j,l,x):
            if s[i] == 1:
                temp_count += 1
        count = max(count,temp_count)
    # print("sdfs",x,count)
    return count

for _ in range(int(input())):
    n = int(input())
    s = [int(x) for x in input()]
    one_c  = sum(s)

    if one_c == 0:
        print(1)
        continue
    if one_c == 1:
        print(0)
        continue

    factors = set()
    for i in range(1,math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)


    ans = sys.maxsize
    
    for i in factors:
        have = {}
        for j in range(i):
            have[j] = sum(s[j:n:i])
        req = n//i
        for j in range(i):
            temp = req-have[j] + one_c - have[j]
            ans = min(ans,temp)
    print(ans)

