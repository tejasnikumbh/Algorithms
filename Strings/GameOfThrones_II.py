# Imports
import math;
def getNumAnag(strDict):
    num = 0;
    denom = [];
    for i in strDict:
        num += strDict[i];
        if(strDict[i]!=0):
          denom.append(strDict[i]);
    numFact = math.factorial(num);
    denomFact = 1;
    for i in range(len(denom)):
        denomFact *= math.factorial(denom[i]);
    result = numFact//denomFact;
    result %= 1000000000 + 7;
    return result;

def genFreqMap(s):
    strDict = {};
    for i in range(len(s)):
        if(s[i] in strDict):
            strDict[s[i]] += 1;
        else:
            strDict[s[i]] = 1;
    for key in strDict:
        if(strDict[key]%2):
            strDict[key] = int((strDict[key]-1)/2);
        else:
            strDict[key] = int(strDict[key]/2);
    return strDict;
        
string = input();
strDict = genFreqMap(string);
anagrams = getNumAnag(strDict);
print(anagrams);
