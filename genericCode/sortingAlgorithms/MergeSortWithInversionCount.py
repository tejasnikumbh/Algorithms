
# ------------------------------------------------------------------- #
# Important things to note in program about the nature of Pythons pass#
# by reference. The array a to be  sorted is a list and is a mutable  #
# type. There fore, when it is passed as a parameter, a reference to  #
# that list object is passed . YOU SHOULD NOT REASSIGN this reference #
# if you want the same a to be altered by the mergesort algorithm in  #
# recursive calls of the sort procedure as well as the merge procedure#
# Note :                                                              #
# This version of mergesort takes an auxilary space of O(N) and is    #
# also good from point of view of brevity                             #
# Reference for Python variable passing Mechanisms:                   #
# http://stackoverflow.com/questions/4344017/how-can-i-get-the-       #
# concatenation-of-two-lists-in-python-without-modifying-either       #
# First Answer with highest upvotes                                   #
# ------------------------------------------------------------------- #

'''
    Function that counts the number of inversions in the array using
    Mergesort .  This reduces the time complexity to count the no of
    inversions and does it in O(NlogN) time
'''
def countInversionsAndSort(a):
    inversions = sort(a,0,len(a)-1)
    return inversions


'''
    Sort Function of mergeSort. According to the recursive substructure
    THe number of inversions is simply inversions in left subarray sort
    + inversions in right subarray sort + inversions done while merging
'''
def sort(a,start,end):
    if(start >= end): return 0
    else:
        midPoint = (start + end) / 2
        inversionsLeft = sort(a,start,midPoint)
        inversionsRight = sort(a,midPoint+1,end)
        inversions = merge(a,start,midPoint,midPoint + 1,end)
        return inversions + inversionsLeft + inversionsRight
    
'''
    Merge function of mergesort in python. The number of inversions
    are incremented here. They are computed by the following logic.
    If an element from right subarray is being merged into the 
    main array a in sorted order, then the number of inversions 
    for each such element being merged from the right subarray
    should be incremented by the elements left in the left subarray
'''
def merge(a,start1,end1,start2,end2):
    merged = [0]*(end2 - start1 + 1)
    count = 0
    inversions = 0
    i = start1
    j = start2
    while(i<=end1 and j<=end2):
        if(a[i]<=a[j]):
            merged[count] = a[i]
            count += 1
            i += 1
        else: #Inversions incremented here
            inversions += (end1 - i + 1)
            merged[count] = a[j]
            count += 1
            j += 1
    while(i<=end1): 
        merged[count] = a[i]
        count += 1
        i += 1
    while(j<=end2): 
        merged[count] = a[j]
        count += 1
        j += 1
    for i in range(start1,end2+1):
        a[i] = merged[i - start1]
    return inversions
        
