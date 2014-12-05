# Importing libraries
import sys
from math import floor

'''
    Main Function to solve the problem
'''
if __name__ == "__main__":
    # Parsing in the input
    [a,b] = [int(x) for x in sys.stdin.readline().rstrip().split()]
    jarAmts = [0]*a
    # Converting to float so that precision is not lost in rounding off
    a = a*1.0
    avg = 0.0;
    for line in sys.stdin:
        [i,j,amt] = [int(x) for x in line.rstrip().split()]
        avg += (j - i + 1)*amt/a     
    # Converting the average to an integer
    avg = int(floor(avg))
    print avg