import sys
from operator import xor
'''
    Function to get the numer. Nothing special in logic. Just regular Xor 
    repeating pattern. Take special care of the case where k > n in which
    case you just need to shift by n times to obtain the number. Hence the
    min(n,k)
'''
def getNum(bitList,n,k):
    numList = []
    numList.append(bitList[0])
    count = 1
    for i in range(1,min(n,k)):
        curBit = xor(bitList[i],bitList[i-1])
        numList.append(curBit)
        count += 1
    
    i = 0
    curBit = numList[i]
    prevVal = bitList[k-1]
    #print numList
    #print bitList
    for j in range(k,n):
        #print "curBit : " + str(curBit) + " prevVal : " + str(prevVal)
        curVal = xor(curBit,prevVal)
        #print "curVal : " + str(curVal)
        bitToAppend = xor(curVal,bitList[j])
        #print "bitToAppend : " + str(bitToAppend)
        numList.append(bitToAppend)    
        i += 1
        curBit = numList[i]
        prevVal = bitList[j]
    return numList

'''
    Main function to run the program
'''
if __name__ == "__main__":
    [n,k] = [int(x) for x in sys.stdin.readline().rstrip().split()]
    bitList =[int(x) for x in list(sys.stdin.readline().rstrip())]
    if(k != 1):
        num = getNum(bitList,n,k)
        num = [str(x) for x in num]
        print ''.join(num)
    else:
        bitList = [str(x) for x in bitList]
        print ''.join(bitList)
