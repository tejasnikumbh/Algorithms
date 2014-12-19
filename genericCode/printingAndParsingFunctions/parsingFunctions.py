'''
    Usage: TO read from files pass in the file stream as follows -  
    E.g -> f = open('filename.txt')
    parseInt(f)     
    To read from standard input stream, use these functions as follows
    E.g -> s = sys.stdin
    parseInt(s)
'''

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
    Reads in an integer from stream passed in as the parameter. Simple
    parsing function that can read from files as well as standard input
''' 
def parseInt(stream):
    return int(stream.readline().rstrip())

'''
    Reads in an array of integers from stream passed in as parameter.This
    is a simple parsing function that can read from files as well as 
    standard input
'''
def parseIntArr(stream):
    return [int(x) for x in stream.readline().rstrip().split()]
 
'''
    Reads in a string from stream passed in as the parameter. Simple
    parsing function that can read from files as well as standard input
'''
def parseString(stream):
    return stream.readline().rstrip()
    
'''
    Reads String array from stream passed in as parameter. Simple parse
    function that can raed from files as well as standard input
'''
def parseStringArr(stream):
    return [str(x) for x in stream.readline().rstrip().split()]
