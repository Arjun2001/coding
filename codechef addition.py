def binaryToDecimal(n): 
    num = n
    dec_value = 0
    base = 1
    temp = num 
    while(temp): 
        last_digit = temp % 10
        temp = int(temp / 10)
        dec_value += last_digit * base
        base = base * 2
    return dec_value

test=int(input())
while(test):
    a=int(input())
    a=binaryToDecimal(a)
    b=int(input())
    b=binaryToDecimal(b)
    ctr=0
    while(b>0):
        u=a^b
        v=a&b
        a=u
        b=v*2
        ctr+=1
    print(ctr)
    test-=1

