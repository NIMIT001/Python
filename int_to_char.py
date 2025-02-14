def fun(n):
    for i in range(0,len(n),2):
        num = int(n[i:i+2])
        char = chr(num)
        print(f"{num}-{char}")





n = input("Enter the values :")
fun(n)
