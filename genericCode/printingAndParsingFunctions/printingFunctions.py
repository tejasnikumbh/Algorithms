'''
    Prints a given grid, given its dimensions and the grid itself
'''
def printGrid(grid,r,c):
    gridStr = ""
    for i in range(r):
        curLine = ""
        for j in range(c):
            curLine += str(grid[i][j]) + " "
        curLine.rstrip()
        gridStr += curLine + "\n"
    gridStr.rstrip()
    print gridStr
        
        
'''
    Function to print the array with numbers in a space seperated format
'''
def printArray(a,delimiter):
    arrayStr = ""
    for i in a:
         arrayStr += str(i) + delimiter
    arrayStr.rstrip()
    print arrayStr
