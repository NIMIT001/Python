def fec(n):
    if n ==0:
        return 1
    else:
       return ((n)*(fec(n-1)))

  
    
n = int(input("Enter : "))
r = fec(n)
print(r)

