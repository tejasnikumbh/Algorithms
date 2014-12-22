# Importing standard libraries
import sys
from math import sqrt

# Parsing functions
def parseInt(stream):
    return int(stream.readline().rstrip())

'''
    
    Dynamically precomputing the summation series for N < 10^6 so that each test case
    is solved in constnat time for any N less than 10^6. There fore for Task 1, this
    solution takes O(1) time
   
'''
# Computing the summation series
def getL(N):
    L = [0]*(N + 1)
    L[1] = 1.0
    for i in range(2, N + 1):
        L[i] = L[i - 1] + sqrt(i * 4.0 - 3.0)
    return L

'''

    For N greater than 10^6 we take an approximation of the series since we have not
    precomputed it already. This approximation was obtained from Wolfram alpha
    
'''
def getAns(N):
    return (4.0/3.0) * (N ** 1.5)
    
# Main function for the program
if __name__ == "__main__":
    stream = sys.stdin
    T = parseInt(stream)
    L = getL(1000000)
    for i in range(T):
        N = parseInt(stream)
        if(N < 1000000):
            summationN = L[N] 
            ans = 0.5 - 1.0/N + (0.5/N) * (summationN)
            print ans
        else:
            summationN = getAns(N)
            ans = 0.5 - 1.0/N + (0.5/N) * (summationN)
            print ans
