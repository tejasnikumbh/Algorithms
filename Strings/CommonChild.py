import sys

def parseString(s):
    return s.readline().rstrip()

'''
    Dynamic Programming Algorithm that finds and returns the length
    of the longest common subsequence given two sequences a and b as
    parameters
'''
def findLCS(a,b):
    
    # Initializing an empty grid for the DP Table
    DPGrid = [[0 for x in range(len(b) + 1)] for x in range(len(a) + 1)]           
    # Filling the grid according to DP algorithm
    for i in range(1,len(a) + 1):
        for j in range(1,len(b) + 1):
            if(a[i - 1] == b[j - 1]):
                DPGrid[i][j] = DPGrid[i - 1][j - 1] + 1
            else:
                DPGrid[i][j] = max(DPGrid[i - 1][j],
                                   DPGrid[i][j - 1])
                
    # Returning the DPGrid length           
    return DPGrid[len(a)][len(b)]

if __name__ == "__main__":
    stream = sys.stdin
    a = parseString(stream)
    b = parseString(stream)
    a = list(a)
    b = list(b)
    result = findLCS(a,b)
    print result
