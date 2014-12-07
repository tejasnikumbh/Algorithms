'''
    Normal Counting sort without any associated array to keep track of
    Time Complexity = O(n)
    Space Complexity = O(n + k)
    Auxilary Space = O(k)
''' 
def countingSort(a):
    b = [0]*(max(a) + 1)
    c = []
    for i in range(len(a)):
        b[a[i]] += 1
    for i in range(len(b)):
        if(b[i] != 0):
            for j in range(b[i]):
                c.append(i)
    return c
