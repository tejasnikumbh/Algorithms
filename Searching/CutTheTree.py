# NOTE : Code Gives Stack Overflow due to a large recursion depth in larger cases.
# However, the same logic in C++ gives no stack overflow. Don't know why that is.
# This code was pretty important from point of view of knowing how to code up
# Node DataStructures etc, therefore, was kept


# Importing standard libraries
import sys
from collections import deque        

'''
    Node class useful for doing computations on trees. Attributes and 
    Methods for the node class are as follows : 
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
        self.curSum = 0
        self.parent = None
        self.children = []
        
    def addChild(self,child):
        child.parent = self
        self.children.append(child)
 


'''
    Reads in an integer from stream passed in as the parameter. Simple
    parsing function that can read from files as well as standard input
''' 
def nextInt(stream):
    return int(stream.readline().rstrip())

'''
    Reads in an array of integers from stream passed in as parameter.This
    is a simple parsing function that can read from files as well as 
    standard input
'''
def nextIntArr(stream):
    return [int(x) for x in stream.readline().rstrip().split()]
        

'''
    Populates the nodeDict . This is basically an adjacency list of the
    nodes represented by the edge connections passed in as the parameter
'''
def populateNodeDict(edgesRaw):
    nodeDict = {}
    for edge in edgesRaw:
        addEdge(nodeDict,edge[0],edge[1])
        addEdge(nodeDict,edge[1],edge[0])
    return nodeDict

'''
    Adds the edge with endpoints n1 and n2 to the node Dictionary. Helps
    in populating the adjacency list
'''
def addEdge(nodeDict,n1,n2):
    if(n1 in nodeDict): nodeDict[n1] += [n2]
    else: nodeDict[n1] = [n2]
    
'''
    Constructs a tree from an adjacency list. Algorithm used is here is
    Breadth First Search. Key steps in this algorithm are maintaining a 
    search BFSQueue and appending and popping from it.
    
    Algorithm Used : Breadth First Search
    Time Complexity : O(N + E), where N is no of Nodes and E edges
    Here E = N - 1 and therefor time complexity is O(N)
'''   
def constructTree(nodeDict,v,rootKey):
    
    # Constructing a tree as a set of vertices
    tree = {}
    for key in nodeDict:
        tree[key] = Node(key,v[key - 1])
        
    treeEdges = []
    # Doing BFS to assign links for the tree as well as add tree edges
    bfsQueue = deque()
    bfsQueue.append(rootKey)
    while(len(bfsQueue) != 0):
        nodeKey = bfsQueue.popleft()
        childrenKeys = nodeDict[nodeKey]
        for childKey in childrenKeys:
            tree[childKey].parent = nodeKey
            tree[nodeKey].addChild(tree[childKey])
            nodeDict[childKey].remove(nodeKey)
            bfsQueue.append(childKey)
            treeEdges.append([nodeKey,childKey])
    return [tree,treeEdges] 

'''
    Computes the curSum of the entire tree using DFS. The only parameter
    that needs to be passed in is the root of the tree. Thereby enabling 
    access to the entire tree
    
    Algorithm Used : Depth First Search
    Time Complexity : O(N + E), where N is no of Nodes and E edges
    Here E = N - 1 and therefor time complexity is O(N)
'''

def computeCurSum(tree,root,visited):
    if(root in visited): return
    if(len(tree[root].children) == 0):
        visited.add(root)
        tree[root].curSum = tree[root].data
    else:
        visited.add(root)
        tree[root].curSum = tree[root].data
        for child in tree[root].children:
            computeCurSum(tree,child.key,visited)
        for child in tree[root].children:
            tree[root].curSum += child.curSum
    
def getRootKey(nodeDict):
    root = -1
    for key in nodeDict:
        if(len(nodeDict[key]) > 1):
            root = key
            break
    return root

'''
    Computes the T Diff by making a cut at the current position as indicated
    by the edge. Returns the answer
'''    
def computeTDiff(tree,rootSum,edge):
    return abs(rootSum - 2*tree[edge[1]].curSum)

if __name__ == "__main__":
    n = nextInt(sys.stdin)
    v = nextIntArr(sys.stdin)
    nodeDict = {}
    edgesRaw = []
    for i in range(n - 1):
        edgesRaw.append(nextIntArr(sys.stdin))
    
    nodeDict = populateNodeDict(edgesRaw)
    rootKey = getRootKey(nodeDict)
    [tree,treeEdges] = constructTree(nodeDict,v,rootKey)
    visited = set()
    computeCurSum(tree,rootKey,visited)
    rootSum = tree[rootKey].curSum
    minTDiff = -1
    count = 0
    for edge in treeEdges:
        if(count == 0):
            minTDiff = computeTDiff(tree,rootSum,edge)
            count += 1
        else:
            curTDiff = computeTDiff(tree,rootSum,edge)
            if(curTDiff < minTDiff):
                minTDiff = curTDiff
    print minTDiff
