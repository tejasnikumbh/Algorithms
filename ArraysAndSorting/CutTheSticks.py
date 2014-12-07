import sys
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    a = [int(x) for x in sys.stdin.readline().rstrip().split()]
    a.sort()
     
    for i in range(len(a)):
        if(a[i] == 0): continue
        stickLen = a[i]
        cuts = 0
        for j in range(i,len(a)):
            if(a[j] - stickLen >= 0):
                a[j] = a[j] - stickLen
                cuts += 1
        print cuts    
        