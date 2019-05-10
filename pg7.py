v=int(input())
a = [int(x) for x in input().split()]
for i in range(0,v):
    if i<v-1:
        k=' '
    else:
        k=''
    if(i!=v-1):
        if i%2==0:
            if a[i]%2!=0:
                print(a[i],end=k)
        elif i%2!=0:
            if a[i]%2==0:
                print(a[i],end=k)
    else:
        if i%2==0:
        if a[i]%2!=0:
            print(a[i],end='')
    elif i%2!=0:
        if a[i]%2==0:
            print(a[i],end='')
