# num = int(input("Enter the Number : "))

# if num ==1:
#     print("its a prime Number")
# if num>1: 
#     for i in range(2,num):
#         if num%i==0:
#          print("Its not a prime Number")
#          break
#     else:
#         print ("Its a prime Number")


# PRINTING RANGE OF PRIME NUMBER

lower = int(input("Enter the lower Number : "))
upper = int(input("Enter the upper Number : "))

for i in range (lower,upper+1):
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)

                
           
