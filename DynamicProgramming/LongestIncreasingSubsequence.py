# Importing standard libraries
import sys

'''
    Reads in an integer from stream passed in as the parameter. Simple
    parsing function that can read from files as well as standard input
''' 
def parseInt(stream):
    return int(stream.readline().rstrip())

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


'''
    O(NlogN) algorithm. Uses the C table computation approach for getting
    the length of the longest Increasing subsequence. The approach is as 
    follows:
    
    In contrast to general dp approach with O(N^2) complexity, the improve
    -ment happens in the second for loop. The loop where we check each element 
    with each preceding element and the corresponding value in its dp array
    Since we check each element with all preceding elements, the complexity is
    O(N^2). We improve this to O(NlogN) by introducing binary search instead
    of the second loop.
    
    We create a new array C. c[i] denotes the minimum last element value of
    all IS with length i. So if A[1...n] is an array of length n and there
    are multiple LIS with length 6, say, then c[6] denotes the minimum ending
    element from this class of increasing sequences. We build c incrementally. 
    
    Initially we consider only the array from A[1..i]. In such a consideration,
    assume we have computed c for such an array. now, let's add A[i+1]. There
    are three cases.
    Case 1: If A[i+1] is less than A[1]. Then it cannot be a part of
    any increasing sequence of length > 1, since it is the minimum element of
    the array and is last in positioning. So, replace c[1] by A[i+1]. And 
    make dp[i+1] equal to 1
    
    Note that : 
    c[1] is always the min elem in the array, because , the min elem of all 
    increasing seq of length 1[the individual elements themselves] is the min
    elem of the array
    
    Case 2 : If A[i + 1] is greater than min elem of longest increasing sequence
    i.e greater than c[LIS length of A[1...n]], then the Longest Increasing sequence 
    of array A[1...i+1] has length more than the A[1...i] and has length equal to
    LIS len of A[1...n] + 1 . So accordingly, we put C[LIS len of A(..i) + 1] to
    A[i+1] and dp[i+1] = LIS len of A(1..i) + 1
    
    Case 3 : If none of the cases hold, we insert A[i+1] by binary search inside 
    the array C.(We do c[k] = A[i+1] if index obtained by binary search is k)
    and update dp array value at index i + 1 to k. We do this because if for an 
    element, the min elem of class of IS is less, we can always obtain an LIS
    greater than that by adding last elem to such a IS of that class.
    
    If you didn't understand jack from this writeup, consult stack overflow or
    some Indian Dude who has a blog on this.
    
'''
def getLISLength(A):
    size = len(A)
    sz = 1
    dp = [1]*len(A)
    c = [0]*len(A)
    c[1] = A[0]
    for i in range(1,size):
        if(A[i] < c[1]):
            c[1] = A[i]
            dp[i] = 1
        elif(A[i] > c[sz]):
            c[sz + 1] = A[i]
            dp[i] = sz + 1
            sz += 1
        else:
            k = binarySearch(c,1,sz,A[i])
            c[k] = A[i]
            dp[i] = k
    return max(dp)

'''
    Main function to run the program
'''
if __name__ == "__main__":
    # Parsing the input
    stream = sys.stdin
    N = parseInt(stream)
    A = []
    for i in range(N):
        A.append(parseInt(stream))
    # Getting the LIS length    
    result = getLISLength(A)
    print result
    
