class pg2:
  def func(n,l):
    t=[]
    if(n==len(l)):
      while(len(l)!=0):
        m=max(l)
        t.append(m)
        l.remove(m)

    print(*t,sep='')

n=int(input())
l=[int(x) for x in input().split()]
pg2.func(n,l)
