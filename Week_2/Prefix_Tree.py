class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.string_tree=[]

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.string_tree.append(word)
        # print(self.string_tree)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # print(word)
        for node in self.string_tree:
            # print("node search")
            # print(node)
            if node==word:
                return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # print("prefix")
        # print(prefix)
        # if len(prefix)==len()
        len_pre=len(prefix)
        for node in self.string_tree:
            # print("node")
            # print(node)
            if node[0:len_pre]==prefix or node==prefix:
                return True
        return False
                
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)