'''
    Generates factors of a particular number by iterating through the num
    upto sqrt(num) . Efficient approach using prime factor generation. The
    function reduce if new to you, just computes result of the supplied
    function f (in this case list.__add__) on the first two elements of the
    supplied list, obtains a result and then performs the same function on
    the result and the next element in the list. In this way it reduces the 
    entire list to one result
'''
def genFactors(n):    
    return set(reduce(list.__add__, 
                [ [i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0 ] ) )
