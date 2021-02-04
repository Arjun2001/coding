from collections import deque
test=int(input())
while(test):
    ctr=0
    st=deque()
    a=input()
    for i in range(0,len(a)):
        if a[i]=='<':
            st.append(a[i])
        else:
            if len(st)>0:
                st.pop()
                ctr+=1
            else:
                st.append("<")
                break
    if len(st)>0:
        print("0")
    else:
        print(2*ctr)
    test-=1
        
