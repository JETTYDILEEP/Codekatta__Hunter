n,m=map(eval,input().split())
l=[]
for x in range(n):
  l.append(list(map(eval,input().split())))
post=[]
arr=[]
temp=[]
t=[]
i=0
j=0
arr.append(l[i][j])
post.append([i,j])
while [n-1,m-1] not in post:
  i=0
  for x in post:
    if x[0]+1<n and x[1]+1<m:
      temp.append(l[x[0]+1][x[1]]+arr[i])
      temp.append(l[x[0]][x[1]+1]+arr[i])
      t.append([x[0]+1,x[1]])
      t.append([x[0],x[1]+1])
    elif x[0]+1<n:
      temp.append(l[x[0]+1][x[1]]+arr[i])
      t.append([x[0]+1,x[1]])
    elif x[1]+1<m:
      temp.append(l[x[0]][x[1]+1]+arr[i])
      t.append([x[0],x[1]+1])
    i+=1
  post=t
  t=[]
  arr=temp
  temp=[]
print(max(arr))
