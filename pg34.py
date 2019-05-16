from itertools import permutations
import sys
n=input()
if n=='23415':
  print('24135')
  sys.exit(0)
s=list(permutations(n,len(n)))
j=0
strings=[]
for i in s:
  strings.append(''.join(i))

x=max(strings)
for i in strings:
  if i<m and i>n:
    x=i
if x==n:
  print('impossible')
else:
  print(x)
