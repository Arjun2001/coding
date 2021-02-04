def prints(stri,n,index,curr):
{
    if (index == n)  
        return; 
   
    cout << curr << "\n"; 
    for (int i = index + 1; i < n; i++) { 
   
        curr += stri[i]; 
        printSubSeqRec(stri, n, i, curr); 
    
        // backtracking 
        curr = curr.erase(curr.size() - 1);  
    } 
    return
} 

test=int(input())
while(test):
    summa=int(input())
    a=input()
    prints(a,a.len(),-1,"")
    ctr1=0
    for i in range(len(a)):
        ctr2=0
        for j in range(i+1,len(a)+1):
            res=a[i:j]
            ctr1=a.count(res)
            ctr1=max(ctr1,ctr2)
    print(ctr1)
    test-=1
