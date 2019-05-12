m,n=map(int,input().split())
a=[]
for _ in range(m):
	b = set(map(int, input().split()))  
	a.append(b)
t=set.intersection(*a)
print(*t)
