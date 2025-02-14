
def fun (ticket, food , coupon, circle):
    cost = 0
    if ticket <5 or ticket > 40:
        print("Min is 5 and max is 40 ")
        return
    if circle == "k":
        cost = ticket * 75
    elif circle == "q":
        cost = ticket*150
    if coupon == 'y':
        if ticket >20 :
            cost = cost * 0.90
        else:
            cost = cost * 0.98
    if food  == 'y':
        cost = cost + ticket*50

    return cost 


    



ticket = int(input("Enter the no. of Tickets : "))
food = input("Enter y on n for food : ")
coupon = input("Enter for coupon : ")
circle  = input("Enter the class : ")
ans = fun(ticket,food, coupon , circle)
print("Ticket cost is : ",ans)
    