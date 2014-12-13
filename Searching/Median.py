from collections import Counter
import decimal
import random

def format_number(num):
    try:
        dec = decimal.Decimal(num)
    except:
        return 'Wrong!'
    tup = dec.as_tuple()
    delta = len(tup.digits) + tup.exponent
    digits = ''.join(str(d) for d in tup.digits)
    if delta <= 0:
        zeros = abs(tup.exponent) - len(tup.digits)
        val = '0.' + ('0'*zeros) + digits
    else:
        val = digits[:delta] + ('0'*tup.exponent) + '.' + digits[delta:]
    val = val.rstrip('0')
    if val[-1] == '.':
        val = val[:-1]
    if tup.sign:
        return '-' + val
    return val

def balanceCounters(medianMore,medianLess,medianMoreSize,medianLessSize):
    if(abs(medianMoreSize - medianLessSize) > 1):
        if(medianMoreSize > medianLessSize):
            elem = min(medianMore.keys())
            medianMore[elem] -= 1
            if(medianMore[elem] == 0):
                del medianMore[elem]
            medianLess[elem] += 1
            return [medianMoreSize - 1,medianLessSize + 1]
        else:
            elem = max(medianLess.keys())
            medianLess[elem] -= 1
            if(medianLess[elem] == 0):
                del medianLess[elem]
            medianMore[elem] += 1
            return [medianMoreSize + 1,medianLessSize - 1]
    else: return [medianMoreSize,medianLessSize]
    
def median(o,e):
    medianLess = Counter()
    medianMore = Counter()
    medianLessSize = 0
    medianMoreSize = 0
    results = []
    sizeElems = 0
    curMedian = -1
    for i in range(N):
        # If we have remove operation
        if(o[i] == 'r'):
            if(sizeElems == 0 or sizeElems == 1):
                if(sizeElems == 1):
                    if(medianLess[e[i]] != 0):
                        del medianLess[e[i]]
                        medianLessSize -= 1
                        sizeElems -= 1    
                    elif(medianMore[e[i]] != 0):    
                        del medianMore[e[i]]
                        medianMoreSize -= 1
                        sizeElems -= 1
                results.append('Wrong!')
                #print "Wrong appended"
            else:
                if(e[i] < curMedian):
                    if(medianLess[e[i]] > 0):
                        medianLess[e[i]] -= 1
                        if(medianLess[e[i]] == 0):
                            del medianLess[e[i]]
                        medianLessSize -= 1
                        sizeElems -= 1
                        # Balancing is important for the code below to hold
                        [a,b] = balanceCounters(medianMore,medianLess,medianMoreSize,medianLessSize)                 
                        medianMoreSize = a
                        medianLessSize = b
                        #print medianMore,medianLess
                        # Find curmedian and append to results
                        if(sizeElems % 2 == 0):
                            left = min(medianMore.keys())/2.0
                            right = max(medianLess.keys())/2.0
                            curMedian = left + right
                            results.append(str(curMedian))
                        else:    
                            curMedian = min(medianMore.keys())
                            results.append(str(curMedian))
                    else:
                        results.append('Wrong!')
                        #print "Wrong Appended"
                elif(e[i] == curMedian):
                    if(medianLess[e[i]] > 0):
                        medianLess[e[i]] -= 1
                        if(medianLess[e[i]] == 0):
                            del medianLess[e[i]]
                        medianLessSize -= 1
                        sizeElems -= 1
                        # Balancing is important for the code below to hold
                        [a,b] = balanceCounters(medianMore,medianLess,medianMoreSize,medianLessSize)                 
                        medianMoreSize = a
                        medianLessSize = b
                        #print medianMore,medianLess
                        # Find curmedian and append to results
                        if(sizeElems % 2 == 0):
                            left = min(medianMore.keys())/2.0
                            right = max(medianLess.keys())/2.0
                            curMedian = left + right
                            results.append(str(curMedian))
                        else:    
                            curMedian = min(medianMore.keys())
                            results.append(str(curMedian))
                    elif(medianMore[e[i]] > 0):
                        medianMore[e[i]] -= 1
                        if(medianMore[e[i]] == 0):
                            del medianMore[e[i]]
                        medianMoreSize -= 1
                        sizeElems -= 1
                        # Balancing is important for the code below to hold
                        [a,b] = balanceCounters(medianMore,medianLess,medianMoreSize,medianLessSize)                 
                        medianMoreSize = a
                        medianLessSize = b
                        #print medianMore,medianLess
                        # Find curmedian and append to results
                        if(sizeElems % 2 == 0):
                            curMedian = min(medianMore.keys())/2.0 + max(medianLess.keys())/2.0
                            results.append(str(curMedian))
                        else:    
                            curMedian = max(medianLess.keys())
                            results.append(str(curMedian))
                    else:
                        results.append('Wrong!')
                        #print "Wrong Appended"                       
                else:    
                    if(medianMore[e[i]] > 0):
                        medianMore[e[i]] -= 1
                        if(medianMore[e[i]] == 0):
                            del medianMore[e[i]]
                        medianMoreSize -= 1
                        sizeElems -= 1
                        # Balancing is important for the code below to hold
                        [a,b] = balanceCounters(medianMore,medianLess,medianMoreSize,medianLessSize)                 
                        medianMoreSize = a
                        medianLessSize = b
                        #print medianMore,medianLess
                        # Find curmedian and append to results
                        if(sizeElems % 2 == 0):
                            curMedian = min(medianMore.keys())/2.0 + max(medianLess.keys())/2.0
                            results.append(str(curMedian))
                        else:    
                            curMedian = max(medianLess.keys())
                            results.append(str(curMedian))
                    else:
                        results.append('Wrong!')
                        #print "Wrong Appended"
        else: # In case we have an append operation
            if(sizeElems == 0):
                medianLess[e[i]] = 1
                medianLessSize += 1
                sizeElems += 1
                curMedian = e[i]
                results.append(str(e[i]))
            else:
                if(e[i] <= curMedian):
                    medianLess[e[i]] += 1
                    medianLessSize += 1
                    sizeElems += 1
                    # Balancing is important for the code below to hold
                    [a,b] = balanceCounters(medianMore,medianLess,medianMoreSize,medianLessSize) 
                    medianMoreSize = a
                    medianLessSize = b
                    #print medianMore,medianLess
                    # Find curMedian and append to results
                    if(sizeElems % 2 == 0):
                        curMedian = min(medianMore.keys())/2.0 + max(medianLess.keys())/2.0
                        results.append(str(curMedian))
                    else:    
                        curMedian = max(medianLess.keys())
                        results.append(str(curMedian))                    
                else:
                    medianMore[e[i]] += 1
                    medianMoreSize += 1
                    sizeElems += 1
                    # Balancing is important for the code below to hold
                    [a,b] = balanceCounters(medianMore,medianLess,medianMoreSize,medianLessSize)                 
                    medianMoreSize = a
                    medianLessSize = b
                    #print medianMore,medianLess
                    # Find curMedian and append to results
                    if(sizeElems % 2 == 0):
                        curMedian = min(medianMore.keys())/2.0 + max(medianLess.keys())/2.0
                        results.append(str(curMedian))
                    else:    
                        curMedian = min(medianMore.keys())
                        results.append(str(curMedian))   
                        
    for result in results:
        print format_number(result)
           
        

N = input()
s = []
x = []
for i in range(0, N):
    tmp = raw_input().strip().split(' ')
    s.append(tmp[0])
    x.append(int(tmp[1]))
    
median(s,x)

