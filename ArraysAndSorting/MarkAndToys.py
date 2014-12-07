'''
    In place quickSort The quickSort Method
	Time Complexity : Best,Avg - O(NlogN) , Worst - O(N^2)
	Space Complexity : O(N)
	Auxilary Space : O(logN) for the stack frames
'''      
def quickSort(a,start,end):
    if(start >= end): return a
    else:
        pivot = a[end]
        swapIndex = start
        for i in range(start,end + 1):
            if(a[i] < pivot): 
                #swap(a,i,swapIndex)
                temp = a[i]
                a[i] = a[swapIndex]
                a[swapIndex] = temp
                swapIndex += 1
        #swap(a,end,swapIndex)
        temp = a[end]
        a[end] = a[swapIndex]
        a[swapIndex] = temp
        quickSort(a,start,swapIndex - 1) 
        quickSort(a,swapIndex + 1,end)
        return a

    
'''
    Function that returns maximum toys that can be bought. Simple strategy is to
    sort the prices array and add as many toys as possible by incrementally adding
    up prices from the least to the most until budget is exhausted. 
'''
def max_toys(prices, rupees):
    #Compute and return final answer over here
    answer = 0
    prices = quickSort(prices,0,len(prices)-1)
    totalBudget = rupees
    for price in prices:
        if((totalBudget - price) >= 0):
            totalBudget -= price
            answer += 1
        else: break        
    return answer

'''
    Main function for the program
'''
if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)
