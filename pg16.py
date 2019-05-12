n,k=map(int,input().split())
l=list(map(int,input().split()))
v=[]
s=""
for i in range(0,len(l)):
    v.append([l[i],abs(l[i]-k)])
v.sort(key=lambda x:x[1])
if v[0][1]==0:
    v.remove(v[0])
for i in range(0,3):
    s=s+str(v[i][0])+" "
print(s.strip())
