class TrieNode:
    def __init__(self):
        self.children = {}
        self.last = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.wordList = []

    def insert(self,arr):
        node = self.root
        for word in arr:
            for c in word:
                if not node.children.get(c):
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.last = True
            node = self.root
    def clear(self):
        self.wordList = []
    
    def autoSuggestion(self,key):
        node = self.root
        for c in list(key):
            if not node.children.get(c):
                return []
            node = node.children[c]
        
        if node.last and not node.children:
            return [key]
        
        return self.getAllSuggestions(node,key)

    def getAllSuggestions(self,node,key):
        if node.last:
            if len(self.wordList) < 3:
                self.wordList.append(key)
        for a,n in node.children.items():
            self.getAllSuggestions(n,key+a)
        return self.wordList

keys = ["mobile","mouse","moneypot","monitor","mousepad"]
key = "mouse"
keys.sort()

t = Trie()
t.insert(keys)
prefix = ''
ans = []
for i in list(key):
    prefix += i
    comp = t.autoSuggestion(prefix)
    ans.append(comp)
    t.clear()
print(ans)
