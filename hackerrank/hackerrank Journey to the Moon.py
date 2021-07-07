class node:
    def __init__(self,parent,rank):
        self.parent = parent
        self.rank = rank
    
def find(subnet,val):
    if subnet[val].parent == val:
        return val
    subnet[val].parent = find(subnet,subnet[val].parent)
    return subnet[val].parent

def join(subnet,u,v):
    p1 = find(subnet,u)
    p2 = find(subnet,v)
    if p1 == p2:
        return
    if subnet[p1].rank > subnet[p2].rank:
        subnet[p2].parent = p1
        subnet[p1].rank += 1
    elif subnet[p1].rank < subnet[p2].rank:
        subnet[p1].parent = p2
        subnet[p2].rank += 1
    else:
        subnet[p2].parent = p1
        subnet[p1].rank += 1

def count(subnet,n):
    count = {}
    for i in range(n):
        temp = find(subnet,i)
        if temp not in count:
            count[temp] = 1
        else:
            count[temp] += 1
    return count

    

n = 4
subnet = []
for i in range(n):
    subnet.append(node(i,0))
ast = [[0,2]]
for i in ast:
    join(subnet,i[0],i[1])
arr = (count(subnet,n))
arr_sum = 0
for i ,j in arr.items():
    arr_sum += j
ans1 = 0
for i,j in arr.items():
    arr_sum -= j
    ans1 += (j*arr_sum)
print("main ans  =",ans1)

# for i in arr:
#     arr_sum -= i
#     ans1 += i*arr_sum
# print(ans1,"ans1",arr,arr_sum)
# ones = 0
# ans = 1
# for i in range(n):
#     if find(subnet,i) == i and arr[i] == 1:
#         ones += 1
# for i in arr:
#     ans *= i
# if ones:
#     ans *= ones
#     ans += ones//2
# print(ans)