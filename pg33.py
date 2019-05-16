n=input()
s=''
m,i=0,0
while i<len(n)-1:
  if n[i]=='a' and n[i+1]=='b':
    s+=n[i]+n[i+1]
    i+=2
  else:
    s=''
    i+=1
  if m<len(s):
    m=len(s)
b=len(n)-1
if n[b]=='a' and n[b-1]=='b' and s!='':
  m+=1
print(m)
