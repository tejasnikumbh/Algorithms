#!/bin/python
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
        printArray(ar," ")
    return ar

'''
    Main function for the program
'''
if __name__ == "__main__":
    m = input()
    ar = [int(i) for i in raw_input().strip().split()]
    insertionSort(ar)
