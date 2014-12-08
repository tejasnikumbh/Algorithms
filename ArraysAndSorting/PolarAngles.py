# Importing standard libraries
import sys
import math
from math import acos
from math import sqrt

        
'''
    Function that returns the polar angle w.r.t origin
'''
def getPolarAngle(x,y):
    dotProduct = x*1 + y*0
    magnitudeProduct = sqrt(x*x + y*y)*1.0
    cosineVal = dotProduct / magnitudeProduct
    theta = math.acos(cosineVal*1.0)
    thetaDegrees = (360 * theta)/(2*math.pi)
    quadrant = getQuadrant(x,y)
    if(quadrant == 3 or quadrant == 4):
        thetaDegrees = 360.0 - thetaDegrees
    if(quadrant == 3 and thetaDegrees == 360.0):
        thetaDegrees = 180.0
    return thetaDegrees

'''
    Gets the quadrant of the corresponding point
'''
def getQuadrant(x,y):
    if(x > 0 and y >= 0):
        return 1
    if(x <= 0 and y > 0):
        return 2
    if(x < 0 and y <= 0):
        return 3
    if(x >= 0 and y < 0):
        return 4
    return -1


'''
    Computed the distance from origin of the point
'''    
def getDistFromOrigin(x,y):
    return sqrt(x*x + y*y)
    
'''
    Main function for the program
'''
if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    pointDes = [[] for x in range(n)]
    for i in range(n):
        [x,y] = [int(x) for x in sys.stdin.readline().rstrip().split()]
        polarAngle = getPolarAngle(x,y)
        dist = getDistFromOrigin(x,y)
        pointDes[i] = [[x,y],polarAngle,dist]
    # A neat trick, courtesy Vijay Suthar, Elec IITB 2015  
    # When two key sorting is used and you want to sort using second key
    # in case first is equal, assign a very high priority to 1st key. It 
    # will order elems properly and effect of secondary key comes into 
    # play only when the first key is EXACTLY the same, which is the case
    # that we want to solve.
    pointDes.sort(key = lambda x: x[1]*10000 + x[2])
    for item in pointDes:
        [x,y] = item[0]
        print str(x) + " " + str(y) + " " 