# Importing libraries
import sys

'''
	Function that iterates through the cases and delegates result for each case 
	to getCount
'''
def getResults(cases):
    results = []
    for case in cases:
        results.append(getCount(case))
    return results

'''
	Function that gets the count for each case
'''
def getCount(case):
    charList = list(case)
    listLen = len(charList)
    count = 0
    for i in range(listLen/2):
        count += abs(ord(charList[i]) - ord(charList[listLen-1-i]))
    return count

'''
	Main function
'''
if __name__ == "__main__":
    # Parsing in input
    t = int(sys.stdin.readline())
    cases = [x.rstrip() for x in sys.stdin.readlines()]
    # Getting the result
    results = getResults(cases)
    # Printing out the results
    for result in results:
        print result