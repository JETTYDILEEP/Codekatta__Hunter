m=input()
l=[]
for i in range(0,len(m)):
    if m[i] not in l:
        l.append(m[i])
for i in range(0,len(l)-1):
    print(l[i],end="")
print(l[-1])    
