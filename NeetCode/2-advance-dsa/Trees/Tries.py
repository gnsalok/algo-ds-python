'''
Time Complexity :-
    Insert Word: O(1)
    Search Word: O(1)
    Search Prefix: O(1)

'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        #  DONT forget to mark work as TRUE in the end.
        # WHY? You inserted "apple" doesn't mean you insert "ap" as well.
        curr.word = True 
        
    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


trie = Trie()
trie.insert("alok")
trie.insert("apple")


print(trie.startsWith("ap"))
print(trie.startsWith("al"))

