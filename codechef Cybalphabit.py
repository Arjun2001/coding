import math
d = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',
     12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',
     23:'x',24:'y',25:'z'}
for _ in range(int(input())):
    n, k = map(int,input().split())
    temp = k
    ele = []
    count = 0
    while(temp > 0):
        temp1 =  int(math.log(temp,2))
        count += 1
        ele.append(temp1)
        temp -= (2**temp1)
    if n < count:
        print('-1')
    elif n==count:
        for i in ele:
            print(d[i],end='')
        print()
    else:
        rem = n-count
        index = 0
        while (rem!=0 and index!=len(ele)):
            if ele[index] == 0:
                index += 1
            else:
                te = ele[index] - 1
                ele[index] = te
                ele.append(te)
                rem -= 1
        if rem == 0:
            for i in ele:
                print(d[i],end='')
            print()
        else:
            print('-1')

                
            
                
            
        
            
            
    
