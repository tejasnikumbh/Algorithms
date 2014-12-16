import sys

def parseInt(s):
    return int(s.readline().rstrip())

def parseString(s):
    return s.readline().rstrip()

def getGems(l):
    uniqueElems = set(l[0])
    for i in range(1,len(l)):
        curElems = set(l[i])
        uniqueElems = uniqueElems.intersection(curElems)
    return len(uniqueElems)

if __name__ == "__main__":
    stream = sys.stdin
    N = parseInt(stream)    
    sList = []
    for i in range(N):
        sList.append(parseString(stream))
    result = getGems(sList)
    print result
    
