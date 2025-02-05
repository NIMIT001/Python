n = int(input("Enter Number : "))
result = list(map(lambda x : x**2,range(n+1)))
print(result)
for i in range(n+1):
    print(result[i], end=" ")