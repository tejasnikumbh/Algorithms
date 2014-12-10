# Importing standard libraries
import sys

'''
    Main function. Nothing special simply follow a greedy strategy of
    arranging the flower costs in descending order and buying in a 
    batch of k flowers at a time
'''
if __name__ == "__main__":
    # Input Parsing
    [n,k] = [int(x) for x in sys.stdin.readline().rstrip().split()]
    a = [int(x) for x in sys.stdin.readline().rstrip().split()]
    # Core Logic - List sort and reversal
    a.sort()
    a.reverse()
    # Buying k batches of flowers at a time
    flowersLeft = n
    cost = 0
    curIndex = 0
    iteration = 1
    while(flowersLeft / k != 0):
        cost += iteration * sum(a[curIndex:curIndex + k])
        curIndex += k
        iteration += 1
        flowersLeft = flowersLeft - k
    cost += iteration * sum(a[curIndex:len(a)])    
    # Pringint the output screen
    print cost