class WordFilter:
    def __init__(self,words):
        self.ptrie = [None] * 27
        self.strie = [None] * 27
        for i in range(len(words)):
            self.insert(words[i],i,self.ptrie)
            self.insert(words[i][::-1],i,self,strie)
    
    def insert(self,word,index,trie):
        for c in word:
            cval = ord(c) - ord('a')
            if not trie[cval] : trie[cval] = [None] * 27
            trie = trie[cval]
            if not trie[26] : trie[26] = []
            trie[26].append(index)

    def retrieve(self,word,trie):
        for c in word:
            cval = ord(c) - ord('a')
            trie = trie[cval]
            if not trie: return []
        return trie[26]
    
    def f(self,pre,suf):
        pvals = self.retrieve(pre,self.ptrie)
        svals = self.retrieve(suf[::-1],self,strie)
        svix,pvix = len(svals) - 1,len(pvals)-1
        while (~svix and ~pvix):
            sval, pval = svals[svix],pvals[pvix]
            if sval == pval: return sval
            if sval > pval: svix -= 1
            else: pvix -= 1
        return -1
