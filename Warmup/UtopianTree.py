# Importing standard libraries
import sys


'''
    Function generates heights for all cycles upto n. n being the max no of cycles in
    input array. Takes linear time
'''
def genTreeHeights(n):
    heights = [1];
    for i in range(1,n+1):
        if(i%2):
            heights.append(2*heights[i-1])
        else:
            heights.append(heights[i-1] + 1)
    return heights

'''
    Main function to run the program
'''
if __name__ == "__main__":
    
    # Parsing the input
    cases = [int(x) for x in sys.stdin.readlines()]
    cases = cases[1:]
    
    # Generate tree heights for all cycles upto max in cases. This avoid unnecessary recomputation
    heights = genTreeHeights(max(cases))
    
    # Access and print relevant results as per cases input
    for case in cases:
        print heights[case]
    