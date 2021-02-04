test=int(input())
a=b=8
while(test):
    chess=[['X' for x in range(a)] for y in range(b)]
    k=int(input())
    chess[0][0]='O'
    move=1
    for x in range(8):
        if move==k:
                break
        for y in range(8):
            if move==k:
                break
            if x!=0 or y!=0:
                chess[x][y]='.'
                move+=1
    for x in range(8):
        for y in range(8):
            print(chess[x][y], end="")
        print()
    test-=1
    
                
            
        
