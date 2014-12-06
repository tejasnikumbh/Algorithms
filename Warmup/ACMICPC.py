# Brute force algo sicne the constraints are pretty small

# Including standard libraries
import sys

'''
    Function that solves the program
'''
def getMaxOr(candidates):
    maxSkills = len(candidates[0])
    # Player indices are hashed to the corresponding entry
    a = [[] for x in range(maxSkills+1)]
    for i in range(len(candidates)):
        for j in range(i+1,len(candidates)):
            skillUnion = genOr(candidates[i],candidates[j])
            a[skillUnion].append([i+1,j+1])
    
    l = maxSkills
    while(l>=0):
        if(len(a[l]) != 0):
            return [l,len(a[l])]
        l -= 1
    return [-1,-1]

'''
    Function that determines the maximal skills of two candidates strings
'''
def genOr(a,b):
    aInt = int(a,2)
    bInt = int(b,2)
    orInt = aInt | bInt 
    orBin = str(bin(orInt)[2:])
    skillsUnion = 0 
    for i in list(orBin):
        if(i == '1'): skillsUnion += 1
    return skillsUnion

'''
    Main function to solve the program
'''
if __name__ == "__main__":
    [n,m] = [int(x) for x in sys.stdin.readline().rstrip().split()]
    candidates = [""]*n
    for i in range(n):
        candidates[i] = sys.stdin.readline().rstrip()
    [maxSkills,numPairs] = getMaxOr(candidates)    
    print maxSkills
    print numPairs
    