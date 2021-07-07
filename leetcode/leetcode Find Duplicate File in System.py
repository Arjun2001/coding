from collections import defaultdict
paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
hashMap ,arr = defaultdict(list),[]
for i in range(len(paths)):
    temp1 = paths[i].split(" ")
    root = temp1[0]
    for j in range(1,len(temp1)):
        temp2 = temp1[j].split('(')
        text = temp2[1][:-1]
        hashMap[text].append(root + "/" + temp2[0])
for v in hashMap.values():
    if len(v) > 1:
        arr.append(v)
print(arr)
