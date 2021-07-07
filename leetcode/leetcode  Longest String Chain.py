from collections import defaultdict
words = ["a","b","ba","bca","bda","bdca"]
W = [ set() for _ in range(17)]
for word in words:
    W[len(word)].add(word)
dp,best = defaultdict(lambda : 1),1
for i in range(16,0,-1):
    if len(W[i-1]) == 0: continue
    for word in W[i]:
        temp = dp[word]
        for j in range(len(word)):
            pred = word[:j] + word[j+1:]
            if pred in W[i-1] and temp >= (dp.get(pred) or 1):
                dp[pred] = temp + 1
                best = max(best,temp + 1)
print(best)