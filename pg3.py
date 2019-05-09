class pg3:
    def func(n,l):
        m=[]
        for i in range(n):
            if(i==l[i]):
                m.append(i)
        m.sort()
        print(*m,sep=' ')
n=int(input())
l=[int(x) for x in input().split()]
pg3.func(n,l)
