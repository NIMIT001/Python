year = int(input("Enter the year : "))
if (year %400 ==0 ) and (year % 100 ==0 ):
    print("Its a leap year")
elif (year %4 == 0 ) and (year % 100 != 0 ):
    print("Its a Leap year")
else:
    print("Its not a Leap Year")
    