# Importing standard libraries
import sys
from operator import xor

'''
    Main function to run the program. For more intuition Draw a Diagram like 
	this. Let us say array = a = [2 1 7 4 5]. + indicates Xor
	2                  1              7          4        5 
	2 + 1              1 + 7          7 + 4      4 + 5 
	2 + 1 + 7          1 + 7 + 4      7 + 4 + 5
	2 + 1 + 7 + 4      1 + 7 + 4 + 5  
	2 + 1 + 7 + 4 + 5
	-------------------------------------------------------------------
	2 + 7 + 5          7 + 5          7 + 5      5        5 = 2 + 7 + 5
    -------------------------------------------------------------------
	Only odd terms remain in case the size of a is odd
	Similarly in case of even size the answer is always 0 [Exercise]
	
	O(N) time algorithm. Fuck yeah I'm smart.
'''
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    for i in range(t):
        n = int(sys.stdin.readline().rstrip())
        a = [int(x) for x in sys.stdin.readline().rstrip().split()]
        if(n % 2 == 0): print 0
        else:
            xorTot = xor(a[0],a[2])
            for i in range(4,n):
                if(i % 2 == 0):
                    xorTot = xor(xorTot,a[i])
            print xorTot