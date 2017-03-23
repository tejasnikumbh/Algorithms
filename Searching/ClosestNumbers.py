# Importing libraries

import sys

'''
    Function to print the array with numbers in a space seperated format
'''
def printArray(a,delimiter):
    arrayStr = ""
    for i in a:
         arrayStr += str(i) + delimiter
    arrayStr.rstrip()
    print arrayStr
    
'''
    Main function to run the program
'''
if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    a = [int(x) for x in sys.stdin.readline().rstrip().split()]
    a.sort()
    diffIndex = []
    minDiff = abs(a[0] - a[0 + 1])
    for i in range(1,len(a) - 1):
        if( abs(a[i] - a[i + 1]) < minDiff):
            diffIndex =  [ a[i], a[i + 1] ] 
            minDiff = abs(a[i] - a[i + 1])
        elif( abs(a[i] - a[i + 1]) == minDiff):
            diffIndex = diffIndex + [ a[i], a[i + 1] ]
    printArray(diffIndex," ")
            
