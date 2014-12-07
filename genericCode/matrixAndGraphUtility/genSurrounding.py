
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

