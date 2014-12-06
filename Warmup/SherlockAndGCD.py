# Importing standard libraries
import sys

'''
    Function that returns a list of prime factors of a number
'''
def genPrimeFactors(n):
    pf = set()
    while(n % 2 == 0):
        pf.add(2)
        n = n/2
    for i in range(3,int(n ** 0.5),2):
        while(n % i == 0):
            pf.add(i)
            n = n/i
    if(n > 2):
        pf.add(n)
    return pf
        
if __name__ == "__main__":
    # Parsing in the number of test cases
    t = int(sys.stdin.readline().rstrip())
    # Iterating through the test cases
    for i in range(t):
        # Parsing in the input
        n = int(sys.stdin.readline().rstrip())
        A = [int(x) for x in sys.stdin.readline().rstrip().split()]
        A = set(A)
        # Generating the prime factors for the numbers as input
        pfs = []
        for elem in A:
            pf = genPrimeFactors(elem)
            pfs.append(pf)
        # Determining common prime factors    
        interSectionSet = set.intersection(*pfs)    
        
        # If common prime factors is an empty set, means there is none
        # divisor that is common than 1 Take care to check about singleton
        # sets while determining this
        if(len(interSectionSet) == 0 and len(pfs) != 1):
            print "YES"
        else:
            print "NO"
                