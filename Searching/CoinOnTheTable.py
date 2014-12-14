# Module import space
import sys

# Global Variable Namespace
N = 0
M = 0
K = 0
grid = []
F = {}
# Function Definition Namespace
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
    The primary logic here is pretty simple. Starting from the position 0,0 and
    number of steps K, we find the optimal solutions by splitting this problem 
    into 4 parts corresponding to each direction in which we can move. We move in
    each direction, decrease the number of steps that we can take, and take the
    minimum of all such direction movements. 
    
    Optimizations : DP table to see if we have already explored a path from a
    particular point on grid. Makes algorithm O(N*M) N and M being dimensions
    
    Edge Cases : Make sure that if we are about to explore a point outside the
    grid, we return an impossible number of steps (K + 1). This is better than
    all the verification that goes into seeing if a point is in a grid or not
    
    Base Case for recursion : Stop when we encounter the '*'
'''
def findOptimalSteps(n,m,k):
    
    # In case the current position is out of the grid 
    if(n<0 or n>=N or m<0 or m >=M): return K+1
    if(k < 0): return K + 1 # If we exhaust number of steps
    
    # Base case for recursion .Returns when star or goal is found
    if(grid[n][m] == '*'): return 0
    
    # Recusrsive steps. Also making sure we dont recompute already computed stuff 
    if((n,m,k) not in F):
        F[(n,m,k)] = min(findOptimalSteps(n - 1,m,k - 1) + (grid[n][m] != 'U'),
                         findOptimalSteps(n + 1,m,k - 1) + (grid[n][m] != 'D'),
                         findOptimalSteps(n,m - 1,k - 1) + (grid[n][m] != 'L'),
                         findOptimalSteps(n,m + 1,k - 1) + (grid[n][m] != 'R'))
        
    # Returning the value from the DP lookup table    
    return F[(n,m,k)]
    
    
# Main Function Namespace  
'''
    Main Function for the program that delegates the work to the function called 
    findOptimalSteps. We start the search at 0,0, with K steps in hand
'''
if __name__ == "__main__":
   
    # Parsing in the input
    stream = sys.stdin
    [N,M,K] = parseIntArr(stream)
    grid = parseGrid(stream,N,M)
    
    # Delegating work to recursive find optimal steps
    optimalSteps = findOptimalSteps(0,0,K)
    
    # Printing output to the console
    if(optimalSteps > K):
        print "-1"
    else:
        print optimalSteps

