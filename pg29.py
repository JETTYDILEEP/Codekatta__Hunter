x = int(input())
l =[int(x) for x in input().split()]
y =max(l)
for i in range(x):
	for j in range(x):
		if (i+j)<=x:
			if y<sum(l[j:((i+j))+1]):
				y = sum(l[j:((i+j))+1])
print(y)
