# Importing standard libraries
import sys

# Parsing Functions
def parseInt(stream):
    return int(stream.readline().rstrip())

'''
    Function that returns the optimal number of candies. This function
    first sorts the rating array A by rating and assigns candies for 
    adjacent people in increasing order
'''
def getCandies(A):
    
    # Sorting by rating
    IndexRating = []
    for i in range(len(A)):
        IndexRating.append([i,A[i]])
    IndexRating.sort(key = lambda x: x[1])
    
    # Assigning optimum candies by building up Candy array dynamically
    CandyArray = [1] * len(A)
    for i in range(len(IndexRating)):
        curIndex  = IndexRating[i][0]
        curRating = IndexRating[i][1]
        curCandies = CandyArray[curIndex]
        nextIndex = curIndex + 1
        prevIndex = curIndex - 1
        
        if(nextIndex < len(IndexRating)):
            nextRating = A[nextIndex]
            nextCandies = CandyArray[nextIndex]
            if(nextRating > curRating and nextCandies <= curCandies):
                CandyArray[nextIndex] = curCandies + 1
                
        if(prevIndex >= 0):    
            prevRating = A[prevIndex]
            prevCandies = CandyArray[prevIndex]
            if(prevRating > curRating and prevCandies <= curCandies):
                CandyArray[prevIndex] = curCandies + 1
            
            
    return sum(CandyArray)
    
    
# Main function for the program
if __name__ == "__main__":
    stream = sys.stdin
    N = parseInt(stream)
    A = []
    for i in range(N):
        A.append(parseInt(stream))
    result = getCandies(A)    
    print result   
    
