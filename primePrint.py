
def shave(n):
    isprime = [True]*(n)
    isprime[0] = isprime[1] = False
    for i in range (2,int(n**0.5)+1):
        if isprime[i]:
            for j in range(i*i,n,i):
                isprime[j] = False
    return [num for num in range(n) if isprime[num]]




def count(n):
    prime = shave(n)
    counts = sum(1 for p in prime if '0' not in str(p))
    return counts




n = int(input("Enter the number : "))
print(count(n))