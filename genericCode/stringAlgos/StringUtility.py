
'''
    
    Tag : Core Generic Function 
    Function that generates a set of all permutations of a given string.
    
'''
def genPerms(s):
    permSet = set()
    # Base case for the Recursion
    if(len(s) == 1):
        permSet.add(s)
        return permSet
    else: # Recursion step
        permSet = genPerms(s[1:])
        curStrSet = set()
        for string in permSet:
            for index in range(len(s)):
                charSet = list(string)         
                charSet.insert(index,s[0])
                curStrSet.add(''.join(charSet))
        return curStrSet
    
'''

	Function that determines if a string is a palindrome or not. 

'''
def isPalindrome(s):
    return s == s[::-1]
