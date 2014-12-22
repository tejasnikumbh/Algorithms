# Importing standard libraries
import sys

# Parsing functions
def parseIntArr(stream):
    return [int(x) for x in stream.readline().rstrip().split()]

# Main function for the program
if __name__ == "__main__":
    # Parsing the input
    stream = sys.stdin
    [A,B,N] = parseIntArr(stream)
    # Dynamically computing the output
    DPTable = [0]*(N + 1)
    DPTable[1] = A
    DPTable[2] = B
    for i in range(3,N + 1):
        DPTable[i] = DPTable[i - 1] * DPTable[i - 1] + DPTable[i - 2]
    # Printing the relevant result (Nth Term)    
    print DPTable[N]    
    
