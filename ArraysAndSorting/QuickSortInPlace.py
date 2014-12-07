# Importing standard libraries
import sys

'''
    Function to print the array with numbers in a space seperated format
'''
def printArray(a,delimiter):
    arrayStr = ""
    for i in a:
         arrayStr += str(i) + delimiter
    arrayStr.rstrip()
    print arrayStr

'''
    In place quickSort The quickSort Method that operates in log(N)
    Auxilary Space. Time Complexity - Avg = O(NlogN), Worst = O(N^2)
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
        printArray(a," ")
        quickSort(a,start,swapIndex - 1) 
        quickSort(a,swapIndex + 1,end)

'''
    Main method to run the program
'''        
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    a = [int(x) for x in sys.stdin.readline().rstrip().split()]
    quickSort(a,0,len(a) - 1)
    