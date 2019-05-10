a,b=map(int,input().split())
a1=[int(x) for x in input().split()]
b1=[int(x) for x in input().split()]
flag=0
if a>b:
  for i in b1:
    if i in a1:
      flag=1
    else:
      flag=0
      break
  if flag==1:
    print('YES')
  else:
    print('NO')
else:
  print('NO')
