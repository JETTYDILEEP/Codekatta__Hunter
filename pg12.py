class pg12:
    def func(k,l):
        
        l.sort()
        l.reverse()
        return l[k-1]
n,k=map(int,input().split())
l=[int(x) for x in input().split()]
print(pg12.func(k,l))
