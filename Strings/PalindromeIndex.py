import sys

def parseInt(stream):
    return int(stream.readline().rstrip())

def parseString(stream):
    return stream.readline().rstrip()

def isPalindrome(s):
    return s == s[::-1]

def makePalindrome(s):
    s = list(s)
    indices = []
    for i in range(len(s)/2 + 1):
        if(s[i] != s[len(s) - 1 - i]):
            indices.append(i)
            indices.append(len(s) - 1 - i)
            break

    i = indices[0]
    j = indices[1]
            
    if(s[i] == s[j - 1] and s[i + 1] == s[j]):
        if(isPalindrome(s[i:j])): return j
        else: return i
    elif(s[i] == s[j - 1]): return j
    else: return i
    
if __name__ == "__main__":
    stream = sys.stdin
    t = parseInt(stream)
    for i in range(t):
        s = parseString(stream)
        if(isPalindrome(s)):
            print "-1"
        else:
            index = makePalindrome(s)
            print str(index)
            
    
