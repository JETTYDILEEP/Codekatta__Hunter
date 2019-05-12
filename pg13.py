class pg13:
    def cunf(s):
            l=[]
            for i in s:
                l.append(i)
            l.reverse()
            m=''
            m=m.join(l)
            if(m==s):
                print('YES')
            else:
                print('NO')
s=input()
pg13.cunf(s)
