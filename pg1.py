n=int(input())
l=[int(x) for x in input().split()]
templi=[]
if(n==len(l)):
  for i in range(0,n):
    if(l.count(l[i])>1 and l[i] not in templi):
      templi.append(l[i])
    else:
      continue
  if(len(templi)==0):
    print('unique')
  else:  
    templi.sort()
    print(*templi,sep=' ')  
