'''
    ------------------------------------------------------------
    Code to traverse a matrix in spiral form. Primarily remember
    to maintain 4 logic variables k,l,m,n indicating lower and 
    upper bounds of rows and cols under iteration respectively
    No recursion. This is an iterative solution
    ------------------------------------------------------------
    Time Complexity = O(MN) where MN is total number of nodes  
    ------------------------------------------------------------
'''
def spiralTraverse(grid):
    # Verifies that the grid is atleast 1X1
    if(len(grid) == 0): return
    if(len(grid[0]) == 0): return 
    # Computes the current rowspan and colspan of matrix    
    [k,l,m,n] = [0,0,len(grid),len(grid[0])]
    spiralMatrix = []
    while(k < m and l < n):
        for i in range(l,n):
            spiralMatrix.append(grid[k][i])
        k += 1
        for j in range(k,m):
            spiralMatrix.append(grid[j][n-1])
        n -= 1
        if(k < m):
            for i in range(n - 1,l - 1,-1):
                spiralMatrix.append(grid[m-1][i])
            m -= 1     
        if(l < n):    
            for j in range(m-1,k - 1,-1):
                spiralMatrix.append(grid[j][l])
            l += 1
    return spiralMatrix        

if __name__ == "__main__":
    grid = [ 
        [1,  2,  3,  4,  5,  6],
        [7,  8,  9,  10, 11, 12],
        [13, 14, 15, 16, 17, 18]
        ]
    spiralTraversed = spiralTraverse(grid)
    print spiralTraversed
                
        