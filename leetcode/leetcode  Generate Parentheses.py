n = 2
def solve(n,s,open_c,close_c,ans,i):
    if open_c == n:
        s += ')' * (n-close_c)
        ans.append(s)
        return
    if open_c < n:
        solve(n,s+'(',open_c+1,close_c,ans,i+1)
        if close_c < open_c:
            solve(n,s+')',open_c,close_c+1,ans,i+1)
    return ans 

print(solve(n,'',0,0,[],0))
    
    
    