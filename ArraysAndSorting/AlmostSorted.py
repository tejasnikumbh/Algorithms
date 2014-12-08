# Importing standard libraries
import sys
# Long Implementation heavy case by case problem
# For fucks sake don't do this if you want to learn more about 
# Algorithms and less about QA
'''
    Returns if the array a is sorted
'''
def isSorted(a):
    isSorted = True
    for i in range(len(a)-1):
        if(a[i+1]<a[i]): 
            isSorted = False
            break
    return isSorted

'''
    Returns swap indices if the swaps make the array sorted. 
    Returns -1 -1 otherwise
'''
def doSwap(a):
    indices = []
    b = []
    c = []
    for i in a:
        b.append(i)
        c.append(i)
        
    for i in range(0,len(a) - 1):
        if(a[i] > a[i+1]):
            temp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = temp
            indices.append(i)
            indices.append(i + 1)
            break
    if(isSorted(a)):
        return indices
    else:
        indices = []
        a = b
        for i in range(0,len(a) - 1):
            if(a[i] > a[i+1]):
                temp = a[i]
                a[i] = a[i + 2]
                a[i + 2] = temp
                indices.append(i)
                indices.append(i + 2)
                break
        if(isSorted(a)):
            return indices
        else:
            flipsAllowed = 2
            a = c
            for i in range(len(a) - 1):
                if(flipsAllowed == 2):
                    if(a[i + 1] < a[i]):
                        begin = i
                        flipsAllowed -= 1
                elif(flipsAllowed == 1):
                    if(a[i + 1] < a[i]):
                        end = i + 1
                        flipsAllowed -= 1
                        break
                        
            if(flipsAllowed == 0):            
                temp = a[begin]
                a[begin] = a[end]
                a[end] = temp
                
            if(isSorted(a)):
                return [begin,end]
            else:
                return [-1,-1]
            
'''
    Returns l to r if revesing makes the list sorted. 
    Returns -1 -1  otherwise
'''        
def doReverse(a):
    indices = []
    flipsAllowed = 2
    begin = -1
    end = -1
    for i in range(len(a) - 1):
        if(flipsAllowed == 2):
            if(a[i + 1] < a[i]):
                begin = i
                flipsAllowed -= 1
        elif(flipsAllowed == 1):
            if(a[i + 1] > a[i]):
                end = i
                flipsAllowed -= 1
                break
    indices = [begin,end]
    a = a[:begin] + list(reversed(a[begin:end+1])) + a[end + 1:]   
    if(isSorted(a)):
        return indices
    else:
        return [-1,-1]
        
            
'''
    Main function for the program
'''
if __name__ == "__main__":
    # Parsing the input
    n = int(sys.stdin.readline().rstrip())
    a = [int(x) for x in sys.stdin.readline().rstrip().split()]
    b = []
    c = []
    for i in a:
        b.append(i)
        c.append(i)
        
    if(isSorted(a)):
        print "yes"
    else:
        
        isSwappable = False
        isReversable = False
        # If swapping was possible set isSwappable to true
        [i,j] = doSwap(b)
        if(i != -1 and j != -1):
            print "yes"
            print "swap " + str(i + 1) + " " + str(j + 1)
            isSwappable = True
        
        # isSwappable being false indicates that the swapping wasnt possible
        [i,j] = doReverse(c)
        if(i != -1 and j != -1 and isSwappable == False):
            print "yes"
            print "reverse " + str(i + 1) + " " + str(j + 1)
            isReversable = True
        # If neither of the above was possible print no
        if(not(isSwappable) and not(isReversable)):
            print "no"
    
        