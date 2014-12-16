import sys

def parseString(stream):
    return stream.readline().rstrip()

def isPangram(string):
    s = list(string)
    f = [False]*26
    for i in s:
        if(i != " "):
            index = ord(i) - ord('a')
            f[index] = True
    for v in f:
        if v == False:
            return False
    return True

if __name__ == "__main__":
    stream = sys.stdin
    string = parseString(stream)
    string  = string.lower()
    if(isPangram(string)):
        print "pangram"
    else:
        print "not pangram"
