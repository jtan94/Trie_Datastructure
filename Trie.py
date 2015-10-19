class Trie:
    class TrieNode:
        def __init__(self,item,next = None, follows = None):
            self.item = item
            self.next = next
            self.follows = follows
            
    def __init__(self):
        self.start = None
    def __insert(node, item):
        if item == "":
            return None
        if node == None:
            node = Trie.TrieNode(item[0])
            node.follows = Trie.__insert(node.follows,item[1:])
            return node
        if node.item == item[0]:
            node.follows = Trie.__insert(node.follows,item[1:])
            return node
        node.next = Trie.__insert(node.next,item)
        return node


    def __contains(node,item):
        if len(item) == 0:
            return True
        if node == None:
            return False
        if node.item == item[0]:
            return Trie.__contains(node.follows,item[1:])
        return Trie.__contains(node.next,item)
    
    def insert(self,item):
        item = item + "$"
        self.start = Trie.__insert(self.start,item)
        
    def __contains__(self,item):
        return Trie.__contains(self.start,item)
    
def main():
    t = Trie()
    f = open('words.txt',"r")
    dictionary = f.readlines()    
    f.close()
    count=0
    
    for x in dictionary:
        count += 1
        x = x.rstrip('\n')
        t.insert(x)
 

    f = open('declarationofindependence.txt')
    words= f.read().replace('-',' ').split()

    for word in words: 
        word = word.replace('.','').replace(',','').replace(';', '').replace(':', '').replace('\'', '').replace('&', '').lower()

        if word not in t:
            print(word)     
    f.close()
    
   
main()
   


        
