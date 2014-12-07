# Importing system libraries
import sys

'''
    Main function for the program
'''
if __name__ == "__main__":
    # Parsing in the input
    [n,k,q] = [int(x) for x in sys.stdin.readline().rstrip().split()]
    a = [int(x) for x in sys.stdin.readline().rstrip().split()]
    qVal = [0]*q;
    for i in range(q): 
        qVal[i] = int(sys.stdin.readline().rstrip())
        
    # Some pre processing    
    k = k % n # Since n Shifts is equal to no shift
    for i in qVal:
        # Taking advantage of the fact that python has 0 indexing
        print a[i - k] 