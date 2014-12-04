# Importing Libraries
import sys

'''
    Function that generates the results for all the test cases. Iterates through
    the test cases and delegates the work ot getCount
'''
def genResults(cases):
    results = []
    for case in cases:
        results.append(getCount(case))
    return results

'''
    Function that coutns the number of deletions required. Marks all required and 
    later retuns the number of them that are required
'''
def getCount(strCase):
    strChars = list(strCase)
    markList = [0]*len(strChars)
    prev = strChars[0]
    for i in range(1,len(strChars)):
        if(strChars[i] == prev):
            markList[i] = 1
        else:
            prev = strChars[i]
    return sum(markList)

'''
    Main Function for the program
'''
if __name__ == "__main__":
    
    # Parsing in input
    t = int(sys.stdin.readline())
    cases = [x for x in sys.stdin.readlines()]
    
    # Generating the results
    results = genResults(cases)
    
    # Printing out results
    for i in results:
        print i