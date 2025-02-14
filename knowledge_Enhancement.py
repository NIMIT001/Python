arr = list(map(int, input("Enter the arr : ").split()))
N = int(input("Enter The Time Limit : "))
n = int(input("Enter arr size : "))
maxi = 0
sorted(arr)
for i in range (0,n):
    if arr[i]<=N :
        maxi+=1
        N = N - arr[i]
print("Max number of book you can read : ",maxi)
