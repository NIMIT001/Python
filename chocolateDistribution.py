n = int(input("Enter : "))
count = 0
MOD = 10**9 +7

for i in range(1,n+1):
    cho = i 
    if (i-1)%5==0 or (i+1)%5==0:
        cho +=2
    count = (count + cho)%MOD
    
print("Output : ",count)


        