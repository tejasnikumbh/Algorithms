#!/bin/python

# Complete the function below.
'''
    Function that computes maximal or of digits in a range
    Logic : firstly, take Xor of least and most elements in range
    Two Cases - Same MSB, Different MSB [in their binary representations]
    If same MSB , then all elements in range have same MSB (since range is l to r)
    So maximal Xor CANNOT have MSB as 1 (since any pair will have same MSB as 1 and
    hence will give a Xor with MSB of 0). 
    If different MSB then Max MSB CAN have 1 as MSB and it MUST since if it does not 
    then simply take Xor of least and most elements. Similar Logic for (MSB +1)th digit
    and so on.
    So answer is simply 2^ position of MSB from right(indexing as 1) - 1
'''

def maxXor(l,r):
    a = l^r
    strLen = len(str(bin(a)[2:]))
    return 2 ** (strLen) - 1

    

_l = int(raw_input());
_r = int(raw_input());

res = maxXor(_l, _r);
print(res)

