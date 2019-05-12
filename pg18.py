n=int(input())
m,o=[],[]
c=0
for i in range(0,n):
  m.append(list(map(int,input().split())))
for i in range(0,n+2):
  if i==0:
    o.append([0]*(n+2))
  elif i==(n+2)-1:
    o.append([0]*(n+2))
  else:
    o.append([0]+m[i-1]+[0])
for i in range(0,len(o)):
    for j in range(0,len(o)):
      if o[i][j]!=0 and n%2==0:
        if o[i-1][j-1]==0 and o[i-1][j]==0 and o[i-1][j+1]==0 and o[i][j-1]==0 and o[i][j+1]==0 and o[i+1][j-1]==0 and o[i+1][j]==0 and o[i+1][j-1]==0:
            c+=1
      elif o[i][j]!=0 and n%2!=0:
        if o[i][j-1]==0 and o[i][j+1]==0 and o[i-1][j]==0 and o[i+1][j]==0:
            c+=1
print(c)
