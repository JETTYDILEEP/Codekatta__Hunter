m=int(input())
l=list(map(int,input().split()))
for i in range(0,m-2):
  for j in range(i+1,m-1):
    for k in range(j+1,m):
      if (l[i]+l[j])==l[k]:
        print(l[i],l[j],l[k])
