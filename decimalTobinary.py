def Convert(n):
    if n>1:
        Convert(n//2)
    print(n%2,end="")
print("The binary of the given number :")
Convert(8)