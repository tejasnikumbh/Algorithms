# Importing standard libraries
import sys

'''
    Produces mincost for the cuts. Follows merge sort's merge procedure after
    sorting the arrays according to the cost (in descending order). Also as the
    elements are merged, corresponding counts are merged (horizontal or vertical)
    and while incrementing the cost, we take note and increment it by the formula
    taking into consideration number of segments the cut is passing through.
    
    Algorithm operates with a greedy strategy. Most Cost first approach.
    Time Complexity : O(M+N)
    
    Note : (A + B) % C = ( A % C + B % C ) % C
'''
def getMinCost(mCost,nCost):
    moduloCon = 1000000000 + 7
    mCuts = 0
    nCuts = 0
    mCost.sort()
    mCost.reverse()
    nCost.sort()
    nCost.reverse()
    mCosti = 0
    nCosti = 0
    totalCost = 0
    while( mCosti < len(mCost) and nCosti < len(nCost) ):
        if(mCost[mCosti] > nCost[nCosti]):
            modInit =  totalCost % moduloCon  + mCost[mCosti]*(nCuts + 1) % moduloCon
            totalCost = ( modInit ) % moduloCon
            mCuts += 1
            mCosti += 1
        else:
            modInit = totalCost % moduloCon +  nCost[nCosti]*(mCuts + 1) % moduloCon
            totalCost = modInit % moduloCon
            nCuts += 1
            nCosti += 1
    while( mCosti < len(mCost) ):         
            modInit =  totalCost % moduloCon + mCost[mCosti]*(nCuts + 1) % moduloCon
            totalCost = modInit % moduloCon
            mCuts += 1
            mCosti += 1
    while( nCosti < len(nCost) ):    
            modInit = totalCost % moduloCon + nCost[nCosti]*(mCuts + 1) % moduloCon
            totalCost = modInit % moduloCon
            nCuts += 1
            nCosti += 1
    return totalCost        

'''
    Main function for the program. Delegates the worki to getMinCost
'''
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    for i in range(t):
        [m,n] = [int(x) for x in sys.stdin.readline().rstrip().split()]
        mCost = [int(x) for x in sys.stdin.readline().rstrip().split()]
        nCost = [int(x) for x in sys.stdin.readline().rstrip().split()]
        minCost = getMinCost(mCost,nCost)
        print minCost