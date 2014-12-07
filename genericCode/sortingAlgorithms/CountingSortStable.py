'''
    Stable Counting Sort which sorts the associated val array according to the
    key values in keyArr, but keeps the ordering of the values for which keys 
    are identical according to the ordering in original array
    Time Complexity = O(n)
    Space Complexity = O(n + k)
    Auxilary Space = O(n + k)
''' 
def countingSortStable(keyArr,valArr):
    b = [[] for x in range(max(keyArr) + 1)]
    c = []
    for i in range(len(keyArr)):
        b[keyArr[i]].append(valArr[i]);
    for i in range(len(b)):
        if(len(b) != 0):
            for j in b[i]:
                c.append(j)
    return c