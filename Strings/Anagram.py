# Importing standard libraries
import sys

'''
    Parsing method that reads and parses and integer from the stream
    passed in as parameter.
'''
def parseInt(s):
    return int(s.readline().rstrip())

'''
    Parsing method that reads and parses a string from the stream that
    is passed in as parameter.
'''
def parseString(s):
    return s.readline().rstrip()


'''
    Method that returns number of edits required to convert string to its
    corresponding valid anagram
'''
def makeAnagram(s):
    s1 = s[:len(s)/2]
    s2 = s[len(s)/2:]
    fs1 = [0]*26
    for i in range(len(list(s1))):
        fs1[ord(s1[i]) - ord('a')] += 1
    for i in range(len(list(s2))):
        fs1[ord(s2[i]) - ord('a')] -= 1
    return sum([x for x in fs1 if x > 0])

'''
    Main function for the program
'''
if __name__ == "__main__":
    stream = sys.stdin
    t = parseInt(stream)
    for i in range(t):
        string = parseString(stream)
        if(len(string) % 2 != 0):
            print "-1"
        else:    
            changes = makeAnagram(string)
            print changes
