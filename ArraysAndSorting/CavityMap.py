# Importing standard libraries
import sys

'''
    Function that generates the valid surrounding indices for a particular index in a grid
    The surroundings are just 4 as of now. But this function can easily be modified by
    modifying the surroundingIndices array
'''
def genSurrounding(grid,i,j):
    validIndices = []
    surrIndices = [ [1,0] , [-1,0] , [0,1] , [0,-1] ]
    if(len(grid) == 0): return -1
    else:
        # Number of rows and columns in grid
        ROWS = len(grid)
        COLS = len(grid[0])
        for [a,b] in surrIndices:
            if((i + a) < 0 or (i + a) >= COLS or (j + b) < 0 or (j + b) >= ROWS): continue
            else: validIndices.append([i + a,j + b])
    return validIndices


'''
    Function that generates the cavity indices with the help of function isCavity
'''        
def genCavityIndices(grid):
    cavityIndices = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            s = genSurrounding(grid,i,j)
            if(isCavity(grid,s,i,j)): 
                cavityIndices.append([i,j])
    return cavityIndices

'''
    Returns if an element is a border element in the grid
'''
def isBorder(grid,i,j):
    ROWS = len(grid)
    COLS = len(grid[0])
    return i == 0 or i == ROWS - 1 or j == COLS - 1 or j == 0 

'''
    Returns if this is cavity by checking condition on surrounding 
    element depths and NOT border condition. Take care of the edge
	condition of only 1 cell in grid. Here, False is returned in
	that case since it is considered border cell
'''
def isCavity(grid,s,i,j):
    elemDepth = int(grid[i][j])
    isThisCavity = True
    for item in s:
        [a,b] = item
        curDepth = int(grid[a][b])
        if(curDepth >= elemDepth or isBorder(grid,i,j)):
            isThisCavity = False
    if(len(grid) == 1): return False
    else: return isThisCavity

'''
    Main function for the program
'''
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    grid = []
    for i in range(t):
        grid.append(list(sys.stdin.readline().rstrip()))
    cavities =  genCavityIndices(grid)  # Generating cavity indices
    
    # Creating the new grid with Xs at apt positions as indicated by
    # the cavities list of cavity indices
    newGrid = grid
    for item in cavities:
        [a,b] = item
        newGrid[a][b] = 'X'
    for i in newGrid:
        print ''.join(i)
    