# Importing library functions
import sys

'''
    Function that determines if such an element exists. Note the time complexity
    It is O(N). Notice how clever I am. 
'''
def doesIndexExist(a):
    if (len(a) == 1):
        return True;
    else:
        leftSum = 0
        index = 0
        rightSum = sum(a[1:])
        while(index != len(a) - 1):
            if(leftSum == rightSum): return True
            else:
                leftSum += a[index]
                index += 1
                rightSum -= a[index]
                
        
    
'''
    Main function of the program
'''
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    for i in range(t):
        n = int(sys.stdin.readline().rstrip())
        a = [int(x) for x in sys.stdin.readline().rstrip().split()]
        if(doesIndexExist(a)):
            print "YES"
        else:
            print "NO"