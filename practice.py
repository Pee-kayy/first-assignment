# height = int(input("please enter hieght in cm: "))
# bill = 0
# if height > 120:
#     print("you can ride")
#     age = int(input("please enter age: "))
#     if age < 12:
#         bill = 5
#         print(f"your bill is {bill}")

#     elif 12<=age<18:
#         bill = 7
#         print(f"your bill is {bill}")

#     else:
#         bill = 12
#         print(f"your fee is {bill}")

#     wants_photo = input("would you like to get a photo during the ride type 'y' fot yes and 'n' for no: ")
#     if wants_photo == "y":
#         bill+=3


#     print(f"your bill is {bill}")

# else:
#     print("can't ride")



# //////////////////////////////////////////PIZZA ORDER SYSTEM/////////////////////////////////////////
pizza_size = input("enter 's'for (small), 'm' for (medium) and 'l' for (large): ")
price = 0
if pizza_size == "s":
    price = 15
    peperoni = input("pepperoni? 'y' for (yes) 'n' for (no): " )
    if peperoni == "y":
        price+=2
        # print(f"total price order is {price}")

elif pizza_size == "m":
    price = 20
    peperoni = input("pepperoni? 'y' for (yes) 'n' for (no): " )
    if peperoni == "y":
        price+=3
        # print(f"total price order is {price}")

elif pizza_size == "l":
    price = 25
    # print(f"total price order is {price}")


cheese = input("cheese? 'y' for (yes) 'n' for (no): " )
if cheese == "y":
    price+=1
    print(f"total price order is {price}")

else:
    print(f"your total price is {price}") 
