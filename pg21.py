n,m=map(int,input().split())
a=[]
for i in range(0,n):
  a.append(list(map(int,input().split())))
for x in range(0,n):
  for y in range(0,m):
    if a[x][y]==0:
      for k in range(0,m):
        a[x][k]=8
      for k1 in range(0,n): 
        a[k1][y]=8
for x in range(0,n):
  for y in range(0,m):
    if a[x][y]==8:
      a[x][y]=0
for i in a:
  print(*i)
