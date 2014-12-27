# Importing standard libraries
import sys
from math import sqrt

# Parsing Functions
'''
    Parses an single integer on a line from given stream be it a file or 
    the standard input.
'''
def parseInt(stream):
    return int(stream.readline().rstrip())



'''
    Getting the number of ways. This follows the recurrence relation, which
    is T(n) = T(n-1) + T(n-4). T(n-1) is the term when we put a vertical
    block in the nth socket and T(n-4) is the term when we put a horizontal
    block in the n-3 through n th socket.
'''
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
       
'''
    Returns number of prime numbers less than or equal to N
'''
def getPrimes(N):
    primeSet = set()
    for i in range(2,N + 1):
        if(isPrime(i)):
            primeSet.add(i)
    return len(primeSet)

'''
    Tests if a number is a prime number.
'''
def isPrime(num):
    for i in range(2,int(sqrt(num) + 1 )):
        if(num % i == 0):
            return False
    return True
         
# Main function for the program            
if __name__ == "__main__":
    stream = sys.stdin
    T = parseInt(stream)
    for i in range(T):
        N = parseInt(stream)
        NWays = getWays(N)
        NPrimes = getPrimes(NWays)
        result = NPrimes
        print result
            
