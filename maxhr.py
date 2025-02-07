arr = list(map(int , input("Enter the arr elements : ").split()))
limit = int(input())
n = int(input("Enter the lenght "))
arr.sort()
count = 0 
for i in range(0,n):
    if arr[i] < limit:
        count +=1
        limit -= arr[i]
print(count)

