a = int(input())
b = int(input())
if a<b:
    smaller = a
else:
    smaller = b
for i in range(1,smaller+1):
    if (a%i==0) and (b%i==0):
        hcf = i

print(hcf)