
import sys

'''
	Function that returns a list of indices in the grid which have
	the specific character supplied as a parameter
'''
def getIndices(grid,character):
    indices = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j] == '#'):
                indices.append([i,j])
    return indices
    
if __name__ == "__main__":
    f = open('square_detector_example_input.txt')
    t = int(f.readline().rstrip())
    for i in range(t):
        n = int(f.readline().rstrip())
        grid = []
        for j in range(n):
            curRow = list(f.readline().rstrip())
            grid.append(curRow)
        filledCells = getIndices(grid,"#")    
        rowIndices = [item[0] for item in filledCells]
        colIndices = [item[1] for item in filledCells]
        minRow = min(rowIndices)
        maxRow = max(rowIndices)
        minCol = min(colIndices)
        maxCol = max(colIndices)
		# Checking if it is a complete rectangle
        isSquare = True
        for j in range(minRow,maxRow + 1):
            for k in range(minCol,maxCol + 1):
                if(grid[j][k] != '#'): isSquare = False
		# Checking if sides of the rectangle are equal		
		if(maxRow - minRow != maxCol - minCol):
			isSquare = False
        if(isSquare):
            print "Case #" + str(i+1) + ": YES"
        else:
            print "Case #" + str(i+1) + ": NO"
