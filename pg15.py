n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(0,n-1):
  if l[i]>max(l[i+1:]):
    s.append(l[i])
s.append(l[n-1])
print(*s)
print(max(l))
