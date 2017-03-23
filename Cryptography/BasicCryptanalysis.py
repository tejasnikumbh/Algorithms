# Importing standard libraries
import sys
import copy

'''
    Basic Cryptanalysis : The logic is pretty simple.
    Step 1: Construct a set of candidate solutions to each words decoded
            message based on length. (Length of encoded and decoded mssage
            is the same)
    Step 2: Try out each path recursively, breaking when inconsistency in
            mapping is encountered. For this the getPath function is used
    Possible Optimization : Sort the word list from largest to smallest
    before performing Steps 1 and Steps 2
'''

'''
    Reads String array from stream passed in as parameter. Simple parse
    function that can raed from files as well as standard input
'''
def parseStringArr(stream):
    return [str(x) for x in stream.readline().rstrip().split()]

'''
    Returns the dictionary list as a set of words by reading from the
    dictionary.lst file
'''
def getDictList(s):
    f = open(s)
    curStr = f.readline().rstrip()
    correctWords = set()
    while(curStr):
        correctWords.add(curStr)
        curStr = f.readline().rstrip()
    return correctWords

'''
    Main function to compute the decoded message.
'''
def convert(inWordList,dictSet):
    # Constructing the candidate set for the conversion
    candidateSet = [set() for i in range(len(inWordList))]
    for i in range(len(inWordList)):
        for j in dictSet:
            if(len(inWordList[i]) == len(j)):
                candidateSet[i].add(j.lower())
    
    index = 0
    outWordList = []
    mapping = {chr(i + ord('a')):'0' for i in range(26)}
    outWordList = getPath(dictSet,inWordList,mapping,candidateSet,index)
    return outWordList

'''
    Recursive function that computes the decoded message
'''
def getPath(dictSet,inWordList,mapping,candidateSet,index):
    if(index >= len(candidateSet)): return [];
    if(len(candidateSet[index]) == 0): return [];
    else:
        candidateSoln = candidateSet[index]
        curWord = inWordList[index]
        maxPath = []
        for soln in candidateSoln:
            if(isValid(mapping,curWord,soln)):
                newMapping = extendMapping(mapping,curWord,soln)
                path = getPath(dictSet,inWordList,newMapping,candidateSet,index + 1)    
                path = [soln] + path
                if(len(path) > len(maxPath)):
                    maxPath = path
        if(len(maxPath) == len(inWordList) - index):
            return maxPath
        else:
            return []

'''
    Function that checks id a particular candidate solution to a particular
    word is a valid mapping and is consistent with previous mapping
'''
def isValid(mapping,curWord,soln):
    for i in range(len(curWord)):
        if(mapping[curWord[i]] != soln[i]):
            if(mapping[curWord[i]] != '0'):
                return False
    return True

'''
    Extends teh current mapping with the mapping from the current solution
    under consideration
'''
def extendMapping(mapping,curWord,soln):
    newMapping = copy.deepcopy(mapping)
    for i in range(len(curWord)):
        newMapping[curWord[i]] = soln[i]
    return newMapping

'''
    Main function to run the program
'''
if __name__ == "__main__":
    stream = sys.stdin
    dictSet = getDictList('dictionary.lst')
    inWordList = parseStringArr(stream)
    outWordList = convert(inWordList,dictSet)
    print ' '.join(outWordList)
    
    
    
''' END '''
