words = ["a","aa","aaa","aaaa"]
words.sort(key=lambda x: len(x),reverse=True)
mask = [0]*len(words)
flag = 1
for i in range(len(words)):
    for ch in words[i]:
        mask[i] |= 1 << (ord(ch) - ord('a'))
    for j in range(i):
        if not mask[i] & mask[j]:
            print(len(words[i])*len(words[j]))
            flag = 0
            break
    if flag == 0:
        break
if flag == 1:
    print('0')




