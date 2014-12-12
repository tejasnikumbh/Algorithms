# Importing standard libraries
import sys
import re

'''
    Function that detects if the regex is part of string and whether
    the positioning is valid
'''
def isValidSubPat(subPatRegex,supPat,R,C,r,c):
    matchPositions = []
    # This is how you get positions of all regex matcches. The specific
    # match can be received by using m.group()
    for m in subPatRegex.finditer(supPat):
        matchPositions.append(m.start())
    if len(matchPositions) == 0:
        return False
    else:
        # We are matching a grid to another grid, so case of overflow
        # needs to be accounted for. [part of string in one row , part in]
        # another
        isPossible = False
        for i in matchPositions:
            if(i % C <= C - c):
                isPossible = True
                break
        return isPossible  
    
'''
    Main function to run the program. The important part of this problem
    is to know how to use variables in REGEX. Other than that, it is a 
    simple regex search problem
'''
if __name__ == "__main__":
    # No of test cases
    t = int(sys.stdin.readline().rstrip())
    for i in range(t): # For each test case
        # Parsing in the input
        [R,C] = [int(x) for x in sys.stdin.readline().rstrip().split()]
        supPat = ""
        for j in range(R):
            supPat += sys.stdin.readline().rstrip()
        [r,c] = [int(x) for x in sys.stdin.readline().rstrip().split()]
        subPat = ""
        patNum = C - c
        for j in range(r):
            if(j != r - 1):
                subPat += sys.stdin.readline().rstrip() + "\d{patNum}"
            else:
                subPat += sys.stdin.readline().rstrip()
            
        # Notice how we replace the string with the variable value
        # This is the highlight of this problem and this is how we
        # use variables in regexes
        subPat = subPat.replace("patNum",str(patNum))
        subPatRegex = re.compile(subPat) # Compiling regex from string   
        
        # Printing output to screen
        if(isValidSubPat(subPatRegex,supPat,R,C,r,c)):
            print "YES"
        else:
            print "NO"
        
