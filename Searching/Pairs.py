'''
    Utility method that does a binarySearch on the sorted array
    a to return the index of the element i in the array. Searches
    the array a in the range (start,end) - both inclusive
    Time Complexity : log(N)
    Returns the Index of the element if found
    Returns -1 other wise
'''
def binarySearch(a,start,end,i):
    # Base case if element not found
    if(start > end): # Equal to step will hold in case size = 1
        return -1
    # Current step for the binary Search
    startElem = a[start]
    endElem = a[end]
    midIndex = (start + end) / 2
    midElem = a[midIndex]
    
    if(i == startElem):
        return start
    if(i == midElem):
        return midIndex
    if(i == endElem):
        return end
    # Recursive steps
    if(i < midElem): # If i lies in left range
        return binarySearch(a,start,midIndex - 1,i)
    elif(i > midElem): # If i lies in right range
        return binarySearch(a,midIndex + 1,end,i)

def pairs(a,k):
    # a contains array of numbers and k is the value of 
    # difference.
    count = 0
    b = []
    
    # Appending elements to b
    for i in a:
        b.append(i + k)
    
    # Preparing a for binary search and searching
    # for all valid elements in b
    a.sort()    
    for i in b:        
        isPresent = binarySearch(a,0,len(a) - 1,i)
        if(isPresent != -1):
            count += 1
    return count
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)

