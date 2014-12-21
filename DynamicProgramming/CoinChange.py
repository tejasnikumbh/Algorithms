# Importing standard libraries
import sys

# Parsing Functions
def parseIntArr(stream,delimiter):
    return [int(x) for x in stream.readline().rstrip().split(delimiter)]

def parseInt(stream):
    return int(stream.readline().rstrip())
'''
    Core Function for the program. The problem is solved using the 
    Dynamic Programming Approach. Following is the recursive sub struc
    -ture.
    Now in including the ith coin for the jth sum,
    Coin change = 1. Include alteast one ith denomination coin 
                + 2. No coin of ith denomination in the sum
    1 -> Solution to problem of upto i denominations, sum = j - ithCoinVal
    2 -> Solution ot problem of upto i - 1 denominations, sum = j
    Imlementational details described in the comments.
    Note that 0,0 in DP table is 1 as described below
'''
def getCoinChangeNum(A,N):
    ans = 0
    # Computing the DP Table for the problem
    DPGrid = [[-1 for x in range(N + 1)] for x in range(len(A) + 1)]
    # Number of coin combinations creating the sum of 0 is always 1,
    # the empty set.
    for i in range( len(A) + 1 ):
        DPGrid[i][0] = 1
    # With 0 coins, no sum can be created except for the number 0
    for i in range(1,N+1):
        DPGrid[0][i] = 0
    # Iteratively computing the solution to this problem. The core
    # DP Algorithm
    for i in range(1,len(A) + 1):
        for j in range(1,N + 1):
            curCoin = A[i - 1]
            curSum = j
            if(curCoin > curSum):
                # If current coin is greater than current Sum, simply 
                # exclude it and fill the grid with the previous result
                # i.e result indicative of num of coinchanges with i - 1
                # coins and same current sum.
                DPGrid[i][curSum] = DPGrid[i-1][curSum]
            else:# Prime recursive step
                excludingCurCoin = DPGrid[i - 1][curSum]
                includingCurCoin = DPGrid[i][curSum - curCoin]
                DPGrid[i][curSum] = excludingCurCoin + includingCurCoin
    
    ans = DPGrid[len(A)][N]       
    return ans

# Main function to run the program
if __name__ == "__main__":
    stream = sys.stdin
    A = parseIntArr(stream,",")
    A.sort()
    N = parseInt(stream)
    result = getCoinChangeNum(A,N)
    print result
