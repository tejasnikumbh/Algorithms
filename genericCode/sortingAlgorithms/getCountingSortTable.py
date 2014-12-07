
'''
    Function that returns the countingSort frequency table
'''
def getCountingSortTable(a):
    maxVal = max(a)
    b = [0]*(maxVal+1)
    for i in range(len(a)):
        b[a[i]] += 1
    return b
