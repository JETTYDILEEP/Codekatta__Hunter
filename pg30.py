n=int(input())
l=[int(x) for x in input().split()]
li=[int(x) for x in input().split()]
c=1
i=0
for j in range(i+1,n):
    if(li[i]<=l[j]):
        c+=1
        i=j
print(c)
