import sys
from math import sqrt

def parseInt(stream):
    return int(stream.readline().rstrip())

def getWays(N):
    if(N >= 4):
        f = [0] *(N + 1)
        f[1] = 1
        f[2] = 1
        f[3] = 1
        f[4] = 2
        for i in range(5 , N + 1):
            f[i] = f[i - 1] + f[i - 4]
        return f[N]
    else:
        if(N < 4):
            return 1
        else:
            return 2
       

def getPrimes(N):
    primeSet = set()
    for i in range(2,N + 1):
        if(isPrime(i)):
            primeSet.add(i)
    return len(primeSet)

def isPrime(num):
    for i in range(2,int(sqrt(num) + 1 )):
        if(num % i == 0):
            return False
    return True
            
if __name__ == "__main__":
    stream = sys.stdin
    T = parseInt(stream)
    for i in range(T):
        N = parseInt(stream)
        NWays = getWays(N)
        NPrimes = getPrimes(NWays)
        result = NPrimes
        print result
            
