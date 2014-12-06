#!/bin/python

# Complete the function below.
'''
    Function that computes maximal or of digits in a range
    Logic : firstly, take Xor of least and most elements in range
    If same MSB , then Xor MSB will be 0 .Similar logic upto MSB 1 in Xor
    When MSB is 1 in Xor, implies least and most range differ in atleast that
    position, least having 0 and most having 1. Even if we include the least
    value of such a range, lets say Xor is 00101, then the l = 00011 and r = 00100
    This is where the flip occurs from 11 to 100 and Xor is maximized. 111. Whose
    value is 2^3 - 1. 
    
    So answer is simply 2^ position of MSB from right(indexing as 1) - 1
    
    Take care of edge case when l = r, in which case return 0
'''

def maxXor(l,r):
    if( l == r): return 0
    a = l^r
    strLen = len(str(bin(a)[2:]))
    return 2 ** (strLen) - 1

    

_l = int(raw_input());
_r = int(raw_input());

res = maxXor(_l, _r);
print(res)

