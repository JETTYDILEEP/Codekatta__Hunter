def reverse(s): 
    w=s.split(" ") 
    e= [i[::-1] for i in w] 
    n= " ".join(e) 
  
    return n
  
  
s=str(input())
print(reverse(s)) 
