# Importing standard libraries
import sys

# Function Namespace
'''
    Populates the nodeDict . This is basically an adjacency list of the
    nodes represented by the edge connections passed in as the parameter
'''
def populateNodeDict(edgesRaw):
    nodeDictLocal = {}
    for edge in edgesRaw:
        addEdge(nodeDictLocal,edge[0],edge[1])
    return nodeDictLocal

'''
    Adds the edge with endpoints n1 and n2 to the node Dictionary. Helps
    in populating the adjacency list
'''
def addEdge(nodeDictLocal,n1,n2):
    if(n1 in nodeDictLocal): nodeDictLocal[n1] += [n2]
    else: nodeDictLocal[n1] = [n2]

'''
    Returns the key of the root of the tree represente by the nodeDict
    dictionary of node to children mapping
'''        
def getRootKey():
    root = -1
    keySet = set()
    childSet = set()
    for key in nodeDict:
        keySet.add(key)
        for child in nodeDict[key]:
            childSet.add(child)
    root = keySet - childSet
    for i in root:
        return i
        
'''
    Reads in an array of integers from stream passed in as parameter.
    This is a simple parsing function that can read from files as well 
    as standard input
'''
def parseIntArr(stream):
    return [int(x) for x in stream.readline().rstrip().split()]
 
def dfs(curRoot,Key):
    if(curRoot not in nodeDict): return 0
    else:
        result = 0
        for child in nodeDict[curRoot]:
            if(abs(child - Key) <= T): 
                result += 1
        for child in nodeDict[curRoot]:
            result += dfs(child,Key)
        return result

# Global Variable Namespace 
N = 0
T = 0
edges = []
nodeDict = {}

'''
    Main Function to run the program
'''
if __name__ == "__main__":
    # Parsing the input 
    stream = sys.stdin
    [N,T] = parseIntArr(stream)
    for i in range(N - 1):
        edges.append(parseIntArr(stream))
    
    # Creating the Tree Datastructure
    nodeDict = populateNodeDict(edges)
    rootKey = getRootKey()
   
    # Obtaining the output using DFS
    result = 0
    for i in range(1,N+1):
        result += dfs(i,i)    
    
    # Prining the output to screen
    print result    
