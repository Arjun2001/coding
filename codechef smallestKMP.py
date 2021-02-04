test=int(input())
while(test):
    import string
    d = dict.fromkeys(string.ascii_lowercase, 0)
    string=input()
    pattern=input()
    start1=pattern[0]
    if len(pattern)>1:
        start2=pattern[1]
    else:
        start2=pattern[0]
    temp=''
    for i in range(len(string)):
        d[string[i]]+=1
    for i in range(len(pattern)):
        d[pattern[i]]-=1
        if start1==start2:
            start2=pattern[i]
    for i in d:
        if (i==start1):
            if (start2<=i or d[i]==0):
                temp+=pattern
                temp=temp+(d[i]*i)
            else:
                temp=temp+(d[i]*i)
                temp+=pattern
        else:
            temp=temp+(d[i]*i)
    print(temp)
    test-=1
