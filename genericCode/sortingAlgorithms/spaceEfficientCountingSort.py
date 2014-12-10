'''
    Space Efficient Counting sort version. Sorts using regular counting sort 
    algorithm except for the fact there is wrapping and unwrapping of vlaues
    in the array to make space efficient frequency Table in the counting sort
    Time Complexity = O(N)
    Space Complexity = O(Max - Min)
'''    
def unWrapIndex(i,minVal):
    return i + minVal

def wrapIndex(i,minVal):
    return i - minVal

def boundCountingSort(a):
    XMin = min(a)    
    XMax = max(a)
    b = [0] * (XMax - XMin + 1)
    for i in a:
        index = wrapIndex(i,XMin)
        b[index] += 1
    sortedArr = []
    for i in range(len(b)):
        for j in range(b[i]):
            element = unWrapIndex(i,XMin)
            sortedArr.append(element)
    return b,sortedArr
