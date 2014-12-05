import sys

'''
    Simple function that generates resutls using the following logic. Computes the 
    sum of stone differences for n possible combinations of a and b differences.
    Take extra care for the fact that same differences obtained should not be returned
    twice, so we put them in a set and returned the elements in sorted order
'''
def genResults(n,a,b):
    resultSet = set()
    for k in range(n):
        curEntry = a*(n-1-k) + b*k
        if(curEntry not in resultSet):
            resultSet.add(curEntry)
    results = []
    for x in resultSet:
        results.append(x)
    results.sort()
    return results
 
'''
    Main Function for the program
'''
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    for i in range(t):
        n = int(sys.stdin.readline().rstrip())
        a = int(sys.stdin.readline().rstrip())
        b = int(sys.stdin.readline().rstrip())
        results = genResults(n,a,b)
        for j in results:
            sys.stdout.write(str(j) + " ")
        sys.stdout.write("\n")