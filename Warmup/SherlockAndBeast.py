# Importing standard libraries
import sys
from math import ceil
from math import floor
from math import sqrt

'''
	Main Function to solve the problem. I am Fucking proud of the size of this.
'''
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    for i in range(t):
        [a,b] = [int(x) for x in sys.stdin.readline().rstrip().split()]
        print int(floor(sqrt(b))) - int(ceil(sqrt(a))) + 1
