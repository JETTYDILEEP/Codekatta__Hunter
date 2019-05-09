class pg4:
    def func(n,l):
        for i in range(n):
            if(l.count(l[i])==1):
                print(l[i])
n=int(input())
l=[int(x) for x in input().split()]
pg4.func(n,l)
