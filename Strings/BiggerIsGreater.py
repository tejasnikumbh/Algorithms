import sys

def parseInt(s):
    return int(s.readline().rstrip())

def parseString(s):
    return s.readline().rstrip()

def convertNum(s):
    sNum = []
    for i in s:
        sNum.append(ord(i) - ord('a'))
    return sNum

def isDescending(numList):
    result = True
    for i in range(len(numList) - 1):
        if(numList[i] < numList[i+1]):
            result = False
            break
    return result
def swap(sList,i,j):
    temp = sList[i]
    sList[i] = sList[j]
    sList[j] = temp
    return sList

def getStr(s):
    sChar = list(s)
    sNum = convertNum(sChar)
    indexPos = []
    if(isDescending(sNum)):
        return "no answer"
    else:
        for i in range(1,len(sNum))[::-1]:
            if(sNum[i] > sNum[i - 1]):
                indexPos.append(i)
                indexPos.append(i - 1)
    charChange = sChar[indexPos[1]]            
    charNumChange = ord(charChange) - ord('a')
    sRightPart = sNum[indexPos[0]:]
    sRightPart.sort()
    for i in range(len(sRightPart)):
        if(sRightPart[i]  > charNumChange):
            temp = sRightPart[i]
            sRightPart[i] = ord(charChange) - ord('a')
            sChar[indexPos[1]] = chr(temp + ord('a'))
            break
    
    sTot = sChar[:indexPos[0]] + toChar(sRightPart)
    return ''.join(sTot)    

def toChar(s):
    for i in range(len(s)):
        s[i] = chr(s[i] + ord('a'))
    return s

if __name__ == "__main__":
    stream = sys.stdin
    n = parseInt(stream)
    for i in range(n):
        s = getStr(parseString(stream))
        print s
