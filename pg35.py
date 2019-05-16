n=input()
l=len(n)//2
m=n[:l]
r=n[l+1:]
if(m==r):
    print("YES")
else:
    print("NO")
