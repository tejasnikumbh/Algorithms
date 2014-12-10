# Importing standarad libraries
import sys

'''
    Brute force solution Takes O(N^2) time. Can use Hashtable 
    to obtain O(N) time complexity given the contraints
'''
def getIndices(a,cost):
    diffArr = [0]*len(a)
    for i in range(len(a)):
        diffArr[i] = cost - a[i]
        
    detected = False
    indices = []    
    for i in range(len(diffArr)):
        if(detected): break
        for j in range(len(a)):
            if(a[j] == diffArr[i] and i != j):
                indices.append(i)
                indices.append(j)
                detected = True
                break
    return indices    
            
'''
    Main function to run the program
'''
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    for i in range(t):
        m = int(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline().rstrip())
        a = [int(x) for x in sys.stdin.readline().rstrip().split()]
        [i,j] = getIndices(a,m)
        print str(i + 1) + " " + str(j + 1)