'''
    In place quickSort The quickSort Method
	Time Complexity : Best,Avg - O(NlogN) , Worst - O(N^2)
	Space Complexity : O(N)
	Auxilary Space : O(logN) for the stack frames
'''      
def quickSort(a,start,end):
    if(start >= end): return a
    else:
        pivot = a[end]
        swapIndex = start
        for i in range(start,end + 1):
            if(a[i] < pivot): 
                #swap(a,i,swapIndex)
                temp = a[i]
                a[i] = a[swapIndex]
                a[swapIndex] = temp
                swapIndex += 1
        #swap(a,end,swapIndex)
        temp = a[end]
        a[end] = a[swapIndex]
        a[swapIndex] = temp
        quickSort(a,start,swapIndex - 1) 
        quickSort(a,swapIndex + 1,end)
