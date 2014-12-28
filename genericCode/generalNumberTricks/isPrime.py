def isPrime(N):
  if(N <= 1): return False
  if(N == 2): return True
  for i in range(2 , int(N ** 0.5) + 1):
    if(N % i == 0): return False
  return True
  
    
