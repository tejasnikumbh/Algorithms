
'''
    Function that generates the valid surrounding indices for a particular index in a grid
    The surroundings are just 4 as of now. But this function can easily be modified by
    modifying the surrIndices array
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

