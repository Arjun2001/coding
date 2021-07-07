# def solve(i,j,k,s1,s2,s3):
#     if k >= len(s3):
#         return 1
#     if i == len(s1) and j == len(s2):
#         return 0
#     if dp[i][j] != -1:
#         return dp[i][j]
#     if i == len(s1) and j != len(s2):
#         dp[i][j] = s2[j:] == s3[k:]
#         return dp[i][j]
#     if i != len(s1) and j == len(s2):
#         dp[i][j] = s1[i:] == s3[k:]
#         return dp[i][j]
#     op1 = op2 = 0
#     if s1[i] == s3[j]:
#         op1 = solve(i+1,j,k+1,s1,s2,s3)
#     if s2[j] == s3[k]:
#         op2 = solve(i,j+1,k+1,s1,s2,s3)
#     dp[i][j] = op1|op2
#     return dp[i][j]



# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"
# if len(s1)+len(s2) != len(s3):
#     print('false')
# dp = [[-1 for x in range(len(s1)+2)] for y in range(len(s2)+2)]
# if(solve(0,0,0,s1,s2,s3)):
#     print('true')
# else:
#     print('false')

def solve(s1,s2,s3):
    if s1 == "" and s2 == "" and s3 == "":
        return True
    if s1 == "" and s2 == "" and s3 != "":
        return False
    if s3 == "" and (s1 != "" or s1 != ""):
        return False
    if dp[len(s1)][len(s2)] != -1:
        return dp[len(s1)][len(s2)]
    if s1 != "":
        if s1[0] == s3[0]:
            # if (solve(s1[1:],s2,s3[1:])):
            #     return True
            dp[len(s1)][len(s2)] = solve(s1[1:],s2,s3[1:])
            if dp[len(s1)][len(s2)]:
                return dp[len(s1)][len(s2)]
    else:
        if (s2 == s3):
            dp[len(s1)][len(s2)] = True
            return dp[len(s1)][len(s2)]
        dp[len(s1)][len(s2)] = False
        return dp[len(s1)][len(s2)]
    if s2 != "":
        if s2[0] == s3[0]:
            # if (solve(s1,s2[1:],s3[1:])):
            #     return True
            dp[len(s1)][len(s2)] = solve(s1,s2[1:],s3[1:])
            if (dp[len(s1)][len(s2)]):
                return dp[len(s1)][len(s2)]
    else:
        if s1 == s3:
            dp[len(s1)][len(s2)] = True
            return dp[len(s1)][len(s2)]
        dp[len(s1)][len(s2)] = False
        return dp[len(s1)][len(s2)]
    dp[len(s1)][len(s2)] = False
    return dp[len(s1)][len(s2)]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
if len(s1)+len(s2) != len(s3):
    print('false')
dp = [[-1 for x in range(len(s2)+2)] for y in range(len(s1)+2)]
if(solve(s1,s2,s3)):
    print("true")
else:
    print("false")