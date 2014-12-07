
'''
    QuickSelect Function that selects kth position element in sorted array using quickSort
    Params : a - array to be sorted
             start - start position of to be sorted subset
             end - end position of to be sorted subset
             pos - the k where we need to find kth element
    Quick Select works on basic principle of recursing on only 1 part of subarray where kth
    element can be present rather recursing on both parts( that the pivot splits the array 
    into ) in Quicksort. 
    Time Complexity : Best - O(1)
                      Avg or Expected - O(N)
                      Worst - O(N^2)
'''
def QuickSelect(a,start,end,pos):
    swapIndex = start
    pivot = a[end]
    for i in range(start,end + 1):
        if(a[i] < pivot): 
            #swap(i,swapIndex)
            temp = a[i]
            a[i] = a[swapIndex]
            a[swapIndex] = temp
            swapIndex += 1
    #swap(swapIndex,end)
    temp = a[swapIndex]
    a[swapIndex] = a[end]
    a[end] = temp
    if(swapIndex == pos):
        return pivot
    elif(swapIndex < pos):
        return QuickSelect(a,swapIndex + 1,end,pos)
    else:
        return QuickSelect(a,0,swapIndex - 1,pos)
