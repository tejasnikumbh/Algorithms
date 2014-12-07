# Importing important libraries
import sys
from collections import deque

'''
    Normal Counting sort without any associated array to keep track of
    Time Complexity = O(n)
    Space Complexity = O(n + k)
    Auxilary Space = O(k)
''' 
def countingSort(a):
    b = [0]*(max(a) + 1)
    c = []
    for i in range(len(a)):
        b[a[i]] += 1
    for i in range(len(b)):
        if(b[i] != 0):
            for j in range(b[i]):
                c.append(i)
    return c


'''
    Stable Counting Sort which sorts the associated val array according to the
    key values in keyArr, but keeps the ordering of the values for which keys 
    are identical according to the ordering in original array
    Time Complexity = O(n)
    Space Complexity = O(n + k)
    Auxilary Space = O(n + k)
''' 
def countingSortStable(keyArr,valArr):
    b = [[] for x in range(max(keyArr) + 1)]
    c = []
    for i in range(len(keyArr)):
        b[keyArr[i]].append(valArr[i]);
    for i in range(len(b)):
        if(len(b) != 0):
            for j in b[i]:
                c.append(j)
    return c

'''
    Main function for the program
'''
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    a = []
    keyArr = []
    for i in range(t):
        curLine = sys.stdin.readline().rstrip().split()
        a.append(int(curLine[0]))
        keyArr.append(curLine[1])
    
    sortedKeyArr = countingSortStable(a,keyArr)
    sortedAArr = countingSort(a)
    
    # Coding up the Twist part. Uses a deque[Double sided queue]
    dashedIndices = [a[x] for x in range(len(a)/2)]
    kMax = max(a)
    dq = [deque() for x in range(max(a) + 1)]
    for i in range(len(sortedAArr)):
        dq[sortedAArr[i]].append(sortedKeyArr[i])
    freqOfDashIndex = [0]*(kMax + 1)
    for i in dashedIndices:
        freqOfDashIndex[i] += 1
    for i in range(len(freqOfDashIndex)):
        if(freqOfDashIndex[i] != 0):
            for j in range(freqOfDashIndex[i]):
                dq[i].popleft()
            for j in range(freqOfDashIndex[i]):
                dq[i].appendleft("-")
     
    # Simply producing the output to print from deque
    strOutput = ""
    for i in dq:
        for j in i:
            strOutput += j + " "
    strOutput = strOutput.rstrip()
    print strOutput
       
    