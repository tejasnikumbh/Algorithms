# Importing standard libraries
import sys
    
'''
    Returns the index of the element in the grid. Element passed in
    must have a unique position. If not present returns [-1, -1]. If
    multiple occurences present, returns the first one
'''    
def findIndex(grid,charElem):    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == charElem):
                return [i,j]
    return [-1,-1]

'''
    Function that generates the valid surrounding indices for a parti
    - cular index in a grid The surroundings are just 4 as of now. But 
    this function can easily be modified by modifying the surrIndices 
    array.
    
    Returns a list of tuples that are indicative of valid indices
'''
def genSurr(grid,i,j):
    validIndices = []
    surrIndices = [ (1,0) , (-1,0) , (0,1) , (0,-1) ]
    if(len(grid) == 0): return -1
    else:
        # Number of rows and columns in grid
        ROWS = len(grid)
        COLS = len(grid[0])
        for (a,b) in surrIndices:
            xIndex = i + a
            yIndex = j + b
            if(xIndex >= ROWS or xIndex < 0):
                continue
            if(yIndex >= COLS or yIndex < 0):
                continue
            validIndices.append((xIndex,yIndex))
    return validIndices

'''
    Returns a list of tuples that belong to the validChars set and have
    not yet been visited (not cointained in visited Set)
'''
def genValidSurr(grid,surr,validChars,visitedSet):
    validSet = []
    for point in surr:
        indexI = point[0]
        indexJ = point[1]
        gridPoint = grid[indexI][indexJ]
        if((gridPoint in validChars) and not(point in visitedSet)):
            validSet.append(point)
    return validSet
        
        
'''
    DFS on a matrix graph/grid which computes one of the Paths from
    start to the goal passed in as parameters. Returns the path as an 
    array of indices from start to goal
    
    Slight Modification for problem [wandUse variable]
    wandUse is used each time we encounter a point from which there are
    variable routes and we know that there exists a path from this point
    till the end
'''
def dfsPathSearch(grid,
                  startIndex,
                  goalIndex,
                  pathSoFar,
                  visitedNodes):
    # Marking the current node as explored
    visitedNodes.add(startIndex)
    # Base case of recursion in case we want to stop 
    # after certain condition
    if(startIndex == goalIndex):
        return True
    else: # Recursive steps
        # Generate all valid surrounding points
        s = genSurr(grid,startIndex[0],startIndex[1])
        validChars = set()
        validChars.add('.')
        validChars.add('*')
        sValid = genValidSurr(grid,s,validChars,visitedNodes)
        # Return False in case no valid surrounding pt found
        if(len(sValid) == 0): return False
        # Iterate through all valid surrouding points
        for point in sValid:
            pathExists = dfsPathSearch(grid,
                                       point,
                                       goalIndex,
                                       pathSoFar,
                                       visitedNodes)  
            if(pathExists):
                # If there were more than one choices here, increment
                # wand use by one
                pathSoFar.append(point)
                return True
        # Return false if no point in valid surroundings
        # can generate a path to goal
        return False    
        
        
                
    
    
'''
    Parses a grid from the passed in stream. Can be used to parse the 
    grid from standard input (by passing in sys.stdin) as well as from
    a text file (by passing in f, where f = open('somename.txt'))
'''
def parseGrid(stream,r,c):
    grid = [[] for x in range(r)]
    for i in range(r):
        grid[i] = list(stream.readline().rstrip())
    return grid
    
'''
    Main Function to run the program. We first find a path using DFS and 
    later compute the number of turns that are necessary (wand usage)
'''    
if __name__ == "__main__":
    # No of test cases
    t = int(sys.stdin.readline().rstrip())
    for i in range(t): # For each test case
        # Parsing the input for the test case
        [r,c] = [int(x) for x in sys.stdin.readline().rstrip().split()]
        grid = parseGrid(sys.stdin,r,c)
        k = int(sys.stdin.readline().rstrip())
        # Exploring and computing the path from start to goal using DFS
        # Path is an array of indices
        startIndex = tuple(findIndex(grid,'M'))
        goalIndex = tuple(findIndex(grid,'*'))
        visitedNodes = set()
        path = []
        dfsPathSearch(grid,
                      startIndex,
                      goalIndex,
                      path,
                      visitedNodes)
        path.append(startIndex)
        path.reverse()
        # Prints the path in order from start to goal
        print path
        
        
