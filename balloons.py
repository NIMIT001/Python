def maxBalloon(A,B,X):
    max_balloon =0
    n = len(A)
    for i in range(n):
        for j in range(i+1,n):
            if B[i] +B[j] <=X:
                max_balloon = max(max_balloon,A[i]+A[j])
    return max_balloon



A = list(map(int,input("Enter the arr A : ").split()))
B = list(map(int,input("Enter the arr B : ").split()))
X = int(input("Enter the Budget : "))
print("Outpt : ",maxBalloon(A, B ,X))
