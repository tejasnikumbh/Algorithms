'''
    Function to print the array with numbers in a space seperated format
'''
def printArray(a,delimiter):
    arrayStr = ""
    for i in a:
         arrayStr += str(i) + delimiter
    arrayStr.rstrip()
    print arrayStr