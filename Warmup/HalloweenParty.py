import sys

'''
    Main Function for the program. Using Python because BigInt usage is required in Java
'''
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    for i in range(t):
        k = int(sys.stdin.readline().rstrip())
        print (k/2)*(k-k/2)