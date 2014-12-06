
'''
    Function that returns a list of prime factors of a number
'''
def genPrimeFactors(n):
	pf = set()
	while(n % 2 == 0):
		pf.add(2)
		n = n/2
	for i in range(3,int(n ** 0.5),2):
		while(n % i == 0):
			pf.add(i)
			n = n/i
	if(n > 2):
		pf.add(n)
	return pf