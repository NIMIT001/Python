n = int(input("Enter : "))
r = n 
sum =0 
while r >0:
    temp = r%10
    cube = temp**3
    sum+= cube
    r//=10

if(sum == n):
    print("Yes! Its Armstrong Number")
else:
    print("No, Its not an Armstrong Number")

