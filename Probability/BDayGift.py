import sys;

n = int(sys.stdin.readline());
S = 0
for i in range(n):
  S += int(sys.stdin.readline());
  
print(S/2.0);
