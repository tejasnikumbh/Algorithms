# Importing standard libraries
import sys

'''
	Main function for the program. 
'''
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    for i in range(t):
        [size,k] = [int(x) for x in sys.stdin.readline().rstrip().split()]
        a = [int(x) for x in sys.stdin.readline().rstrip().split()]
        b = [int(x) for x in sys.stdin.readline().rstrip().split()]
        for i in range(len(b)):
            b[i] = k - b[i]
        a.sort()
        b.sort()
		
		# Even if one of these is less than corresponding element in b, then
		# there is no way any that this can be true. Think
        doesExist = True
        for i in range(len(b)):
            if(a[i] < b[i]): doesExist = False
        if(doesExist):
            print "YES"
        else:
            print "NO"
        