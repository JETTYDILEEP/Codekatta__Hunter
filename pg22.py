m=int(input())
a=list(map(int,input().split()))
out=[]
for i in range(m):
    s=1
    for j in range(m):
        if i!=j:
            s=s*a[j]
    out.append(s)
x=len(out)
for i in range(x):
    if i!=x-1:
        print(out[i],end=' ')
    else:
        print(out[i])
