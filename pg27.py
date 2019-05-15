x=str(input())
f=1
n=len(x)
while(n>0):
    re=x[::-1]
    if(x==re):
        n = len(x)
        x = x[:n - 1]
    else:
        f = 0
        print(x)
        break
