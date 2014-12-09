# Importing standard libraries
import sys

'''
    Function that computes the pMean for the very first position
'''
def getPMean(a):
    if(len(a) == 1): return a
    else: return sum([ a[i]*(i+1) for i in range(len(a)) ])
    

'''
    Main function of the program. Take care of the case when 
	the pMeanMax can be -ve
'''
if __name__ == "__main__":
    # Parsing the input
    n = int(sys.stdin.readline().rstrip())
    a = [int(x) for x in sys.stdin.readline().rstrip().split()]
    # Computing pMeans for current position 
    pMean = getPMean(a)
    pMeanMax = pMean; # Needs to be intialized since it can be -ve
    
    # Computing the sum of all the elems on the conveyor belt
    pSum = sum(a)
    # Now we compute max sum by iterating ONCE through the array,
    # by decreasing pMean by SUm and adding N*a[i] in each step
    for i in a:
        curPMean = pMean - pSum + n*i
        pMean = curPMean
        if(curPMean > pMeanMax): pMeanMax = curPMean
    # Priniting max pMeans    
    print pMeanMax