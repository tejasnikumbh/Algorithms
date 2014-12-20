N = int(input());
def decodeWord(key,string):
    alphabet =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    listStr = list(string);
    newStr = [];
    for i in range(len(listStr)):
        index = key.index(listStr[i]);
        newStr.append(alphabet[index]);
    return ''.join(newStr);

def getKey(keyWord):
    
    """ Function returns the substitution key according to the algo defined in ...
        ... problem statement """
    
    key = {};
    
    # Getting the unique keyword
    uniqueWord = [];
    for i in range(len(keyWord)):
        if(not(keyWord[i] in uniqueWord)):
            uniqueWord.append(keyWord[i]);
    
    # Producing the substitution
    rowLen = len(uniqueWord);
    
    colsA = [];
    cols2 = [];
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
    for i in range(len(alphabet)):
        if(alphabet[i] not in uniqueWord):
            cols2.append(alphabet[i]);
        else:
            colsA.append(alphabet[i]);
            
    cols1 = uniqueWord + cols2;
    
    l1=[];
    l2=[];
    l3=[];
    l4=[];
    l5=[];
    l6=[];
    l7=[];
    
    for i in range(len(cols1)):
        if(i%rowLen==0):
            l1.append(cols1[i]);
        elif(i%rowLen==1):
            l2.append(cols1[i]);
        elif(i%rowLen==2):
            l3.append(cols1[i]);
        elif(i%rowLen==3):
            l4.append(cols1[i]);
        elif(i%rowLen==4):
            l5.append(cols1[i]);
        elif(i%rowLen==5):
            l6.append(cols1[i]);
        else:
            l7.append(cols1[i]);
    l = [];
    for i in range(rowLen):
        if(colsA[i] in l1):
            l= l + l1;
        if(colsA[i] in l2):
            l= l + l2;
        if(colsA[i] in l3):
            l= l + l3;
        if(colsA[i] in l4):
            l= l + l4;
        if(colsA[i] in l5):
            l= l + l5;
        if(colsA[i] in l6):
            l= l + l6;
        if(colsA[i] in l7):
            l= l + l7;
    
    return l;      
    
for i in range(N):
    # Taking in the input
    keyWord = (input());
    crypt = (input().split());
    
    # Getting the substitution key
    key = getKey(keyWord);
    
    decrypt = [];
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];

    # Decoding the crypt
    for i in range(len(crypt)):
        decoded = decodeWord(key,crypt[i]);
        decrypt.append(decoded);
        
    print(' '.join(decrypt));     
    
    
