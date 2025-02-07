def fun(S):
    n = len(S)
    max_dis = 0 
    for i in range(0,n):
        for j in range(i+1,n):
            if S[i] != S[j]:
                
                max_dis = max(max_dis,j-i)
    return max_dis






s = input("Enter the string : ")
print("The max distance is : ", fun(s))
