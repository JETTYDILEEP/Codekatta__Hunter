n=int(input())
l=[int(x) for x in input().split()]
l1=[]
test=0
for i in l:
    if i not in l:
        l.append(i)
    else:
        print(i)
        test+=1
        break
if test==0:
    print("unique")
