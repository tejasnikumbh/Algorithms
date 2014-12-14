
'''
    Node class useful for doing computations on trees. Attributes and 
    Methods for the node class are as follows : A Node is also a tree
    since it has recursive definition.
    Attributes : 
        key - key of the node
        data - data at node
        curSum - sum of tree rooted at node
        parent - pointer to parent Node
        children - list of poitners to children
    Methods : 
        addChild()
            - Adds a child to the current node
'''
class Node:
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.parent = None
        self.children = []
        
    def addChild(self,child):
        child.parent = self
        self.children.append(child)
 
