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
