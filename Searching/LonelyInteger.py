#!/usr/bin/py
'''
    Method uses Hashtable technique since the entries are bound. Time
    Complexity of this method is O(N)
'''
def lonelyinteger(a):
    hashTable = [0]*(101)
    for i in a:
        hashTable[i] += 1
    for i in range(len(hashTable)):
        if(hashTable[i] % 2 == 1):
            return i
        
        
'''
    Main function to run the program
'''  
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
