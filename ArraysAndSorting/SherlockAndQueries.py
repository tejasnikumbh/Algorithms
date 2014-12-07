# Importing standard libraries

'''
    Function to print the array with numbers in a space seperated format
'''
def printArray(a,delimiter):
    arrayStr = ""
    for i in a:
         arrayStr += str(i) + delimiter
    arrayStr.rstrip()
    print arrayStr
    
'''
    Main function for the program
'''
if __name__ == "__main__":
    f = open('input1.txt')
    # Parsing the input
    arr = [int(x) for x in f.readline().rstrip().split()]
    n = arr[0]
    m = arr[1]
    a = [int(x) for x in f.readline().rstrip().split() ]
    b = [int(x) for x in f.readline().rstrip().split() ]
    c = [int(x) for x in f.readline().rstrip().split() ]
    # Constant for modulo
    moduloCon = 1000000007
    k = []
    for i in b:
        k.append(range(i,n+1,i))
    for i in range(len(k)):
        for j in range(len(k[i])):
            a[k[i][j]-1] = ( (a[k[i][j]-1] ) * (c[i] ) ) % moduloCon
    #printArray(a," ")
	