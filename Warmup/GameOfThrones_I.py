''' 
    Does a counting sort on the String to make a frequency table
    Post that, this function determines if a palindorme is possible
    with the permuntations of the string using modulo 2 logic
'''
def isKey(string):
    alphaFreq = [0]*26
    for i in list(string):
        alphaFreq[ord(i)-ord('a')] += 1;
    count = 0;
    for i in alphaFreq:
        if(i%2):
            if(count == 0):
                count += 1
            else:
                return False
    return True

'''
    Main Function to run the program
'''
if __name__ == "__main__":
    string = raw_input().rstrip()
    if(isKey(string)):
        print "YES"
    else:
        print "NO"