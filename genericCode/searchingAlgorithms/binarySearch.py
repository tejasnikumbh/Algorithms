
'''
    Utility method that does a binarySearch on the sorted array
    a to return the index of the element i in the array. Searches
    the array a in the range (start,end) - both inclusive
    Time Complexity : log(N)
    Returns the Index of the element if found
    Returns index of immdiately greater element otherwise
'''
def binarySearch(a,start,end,i):
    # Base case if element not found
    if(start > end): # Equal to step will hold in case size = 1
        return start
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
