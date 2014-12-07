# Importing standard libraries
import sys

'''
    Function that returns the countingSort frequency table
'''
def getCountingSortTable(a):
    maxVal = max(a)
    b = [0]*(maxVal+1)
    for i in range(len(a)):
        b[a[i]] += 1
    return b

'''
    Main Function to run the program
'''
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    for i in range(t):
        n = int(sys.stdin.readline().rstrip())
        a = [int(x) for x in sys.stdin.readline().rstrip().split()]
        table = getCountingSortTable(a)
        indices = 0
        for entry in table:
            if(entry != 0):
                # Factor of divide by 2 is missing in NC2 because every 
                # pair is counted twice. (i,j) and (j,i)
                indices += (entry*entry - entry)
        print indices