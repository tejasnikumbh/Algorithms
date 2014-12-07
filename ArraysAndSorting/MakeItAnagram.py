# Importing standard libraires
import sys

'''
    Main Function for the program. Logic is as follows
    Make two frequency tables for two strings
    Take overlap of both and add up the non overlapping regions (absolute values)
'''
if __name__ == "__main__":
    # Parsing in the input
    s1 = list(sys.stdin.readline().rstrip())
    s2 = list(sys.stdin.readline().rstrip())
    # Initialize the character array as a hashtable
    charFreqs1 = [0]*26
    charFreqs2 = [0]*26
    anagram = [0]*26
    # Record frequencies of characters in s1 and s2
    for i in s1:
        charFreqs1[ord(i) - ord('a')] += 1
    for i in s2:
        charFreqs2[ord(i) - ord('a')] += 1 
    for i in range(26):
        anagram[i] = abs(charFreqs1[i] - charFreqs2[i])
    print sum(anagram)
