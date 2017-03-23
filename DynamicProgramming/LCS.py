# Importing standard libraries
import sys

# Parsing functions
def parseIntArr(stream):
    return [int(x) for x in stream.readline().rstrip().split()]

# Printing functions
def printArr(arr):
    output = ""
    for i in arr:
        output += str(i) + " "
    output.rstrip()
    return output

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
    
    Core Function. Computes the LCS for two sequences passed in as 
    parameters. Follows Dynamic Programming approach. If you want all
    the sub sequences, just do dfs on all paths and append both indices
    as described in comments, while creating the Backpointer grid.
    
'''
def findLCS(A,B):
    
    DPGrid = [[-1 for x in range(len(A) + 1)] for x in range(len(B) + 1)]
    BPGrid = [[-1 for x in range(len(A) + 1)] for x in range(len(B) + 1)]
    for i in range(len(B) + 1):
        DPGrid[i][0] = 0
        BPGrid[i][0] = None
    for i in range(len(A) + 1):
        DPGrid[0][i] = 0
        BPGrid[0][i] = None
    for i in range(1,len(B) + 1):
        for j in range(1,len(A) + 1):
            if(A[j - 1] == B[i - 1]):
                DPGrid[i][j] = 1 + DPGrid[i - 1][j - 1] 
                BPGrid[i][j] = (i-1,j-1)
            else:
                DPGrid[i][j] = max(DPGrid[i - 1][j],DPGrid[i][j - 1])
                if(DPGrid[i][j-1] == DPGrid[i - 1][j]):
                    # Would be a list [(i-1,j),(i,j-1)] if we needed all LCS
                    BPGrid[i][j] = (i-1,j)
                elif(DPGrid[i][j-1] > DPGrid[i - 1][j]):
                    BPGrid[i][j] = (i,j-1)
                else:
                    BPGrid[i][j] = (i-1,j)
    
    # Create an index list of backpointers
    indexList = []
    iterElem = BPGrid[len(B)][len(A)]
    indexList.append(iterElem)
    while(iterElem[0] != 0 and iterElem[1] != 0):
        iterElem = BPGrid[iterElem[0]][iterElem[1]]
        indexList.append(iterElem)
        
    # Creating the LCS. Appending elements where mismatch happens
    LCS = []
    for i in range(len(indexList) - 1):
        curElem = indexList[i]
        nextElem = indexList[i + 1]
        if ( nextElem[0] == (curElem[0] - 1) and nextElem[1] == (curElem[1] - 1)):
            LCS.append(B[curElem[0] - 1])
    return reversed(LCS)
        
# Main function for the program
if __name__ == "__main__":
    stream = sys.stdin
    [M,N] = parseIntArr(stream)
    A = parseIntArr(stream)
    B = parseIntArr(stream)
    result = findLCS(A,B)
    resultStr = printArr(result)
    print resultStr

'''END'''
