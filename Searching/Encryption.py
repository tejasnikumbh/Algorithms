# Importing standard libraries
import sys
from math import ceil
from math import floor
from math import sqrt

'''
    Main function t run the program. The only important thing in
    this question is to actually understand what the questions
    means. Use the examplify approach to see what it acutally
    means and proceed accordingly.
    
    Note : Ceil and Floor of same num can at max have diff of 1
'''
if __name__ == "__main__":
    # Parsing in the input
    string = sys.stdin.readline().rstrip()
    strList = list(string)
    charNum = len(strList)
    # Deciding on the width and height bounds
    widthLower = int(floor(sqrt(charNum)))
    heightHigher = int(ceil(sqrt(charNum)))
    height = width = -1
    # The case of a square
    if(widthLower == heightHigher):
        width = widthLower
        height = heightHigher
    else: # The case of a rectangle    
        # In case the number of characters dont fit in,
        # increase the width to convert it into a square
        if(widthLower * heightHigher < charNum):
            width = widthLower + 1
            height = heightHigher
        else: # Else increase the width and decrease the height
            width = widthLower + 1
            height = heightHigher - 1
    # Once height and width is set, we encode the message
    outputList = [[] for x in range(width)]        
    for i in range(len(strList)):
        category = i % width
        outputList[category].append(strList[i])
    # Printing the output to console
    outputStr = ""
    for i in outputList:
        outputStr += ''.join(i) + " "
    print outputStr
            
    
    