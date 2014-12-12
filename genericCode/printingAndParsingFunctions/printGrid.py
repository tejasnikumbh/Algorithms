'''
    Parses a grid from the passed in stream. Can be used to parse the 
    grid from standard input (by passing in sys.stdin) as well as from
    a text file (by passing in f, where f = open('somename.txt'))
'''
def parseGrid(grid,r,c):
    gridStr = ""
    for i in range(r):
        curLine = ""
        for j in range(c):
            curLine += grid[i][j] + " "
        curLine.rstrip()
        gridStr += curLine + "\n"
    gridStr.rstrip()
    print gridStr
        
        
