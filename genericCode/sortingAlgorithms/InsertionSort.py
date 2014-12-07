'''
    Function for insertion sort
    Time Complexity : O(N)
    Space Complexity : O(N)
    Auxilary Space : O(1)
'''    
def insertionSort(ar):    
    for i in range(1,len(ar)):
        j = i - 1
        elem = ar[i]
        while(j >= 0 and ar[j] > elem):
            ar[j + 1] = ar[j]
            j -= 1
        ar[j + 1] = elem
    return ar