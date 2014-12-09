# Importing standard libraries
import sys

'''
    Function to check if factors are ones that are possible. Performs the
    core logic to check if the particular factor is a possible capacity
'''
def checkFactors(a,factors):
    possibleCaps = []
    for factor in factors:
        if(checkFactor(a,factor)):
            possibleCaps.append(factor)
    return possibleCaps

'''
    Check if a particular factor is a possible capacity. It iterates through
    the entire array of buses and returns true if that factor capacity holds
'''
def checkFactor(a,factor):
    availSpace = factor
    for group in a:
        availSpace -= group
        if(availSpace < 0): return False
        elif(availSpace == 0): availSpace = factor
    availSpace -= factor
    if(availSpace == 0): return True
    elif(availSpace < 0): return False
    
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
    Generates factors of a particular number by iterating through the num
    upto num / 2 . Efficient approach using prime factor generation
'''
def genFactors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

'''
    Main function for the program
'''
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    a = [int(x) for x in sys.stdin.readline().rstrip().split()]
    minCap = max(a)
    maxCap = sum(a)
    factors = genFactors(maxCap)
    #print factors
    
    factors = [x for x in factors if x>= minCap and x<=maxCap]
    #print factors
    
    possibleCaps = checkFactors(a,factors)
    possibleCaps.sort()
    #print possibleCaps
    printArray(possibleCaps," ")