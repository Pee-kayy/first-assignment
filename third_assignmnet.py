#with this set of tasks i was able to combine my previous knowledge such as strings and string manipulation, type conversion,
# f strings to newly learnt skills such as conditional statements 
# (if else, elif ) and comparison operators




#1. this peice of code checks if the user is eligible to vote or not
age=int(input("please enter your age: \n"))
if age >= 18:
    print("you're eligble to vote")
else:
    print("You're not elible to vote")

    #2. write a code that compares two numbers entered by the user and prints which is greater of if they're equal
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")

elif num2 > num1:
    print(f"{num2} is greater than {num1}")

else:
    print("the two numbers are equal")

#3. this code checks if a number is positive negative or zero
number = float(input("enter number: "))
if number >= 0:
    print("its a positive number")
else:
    print("its a negative number")

#4. a code that prints students score
score = float(input("enter students sscore: "))
 
if score >= 70:
    print("distinction")

elif score >=50 <=69:
    print("pass")


else:
    print("fail")

#5 this code checks if a number is even or odd
num = float(input("enter number: "))

if num % 2 == 0:
    print("even number")

else :
    print("odd number")

   
