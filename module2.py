# # coding exercise
# # Q1
# num1 = float(input("enetr num1 :"))
# num2 = float(input("enter num2 :"))
# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2
# print(addition)
# print(subtraction)
# print(multiplication)
# print(division)

# # Q2
# num = int(input("enter number"))
# if num % 2 == 0:
#     print("number is even")
# else :
#     print("number is odd")

# # Q3
# item_price = float(input("enter item's price :"))
# quantity = int(input("enter item's quantity :"))
# total_bill = item_price * quantity
# print(total_bill)

# # Q5
# student_marks = float(input('enter your marks :'))
# if student_marks >= 40 and student_marks <100 :
#     print("passed")
# elif student_marks <= 40 and student_marks >= 0 :
#     print("failed")
# else :
#     print("invalid marks")


# assignment operator
# f = 6
# f**= 4
# print(f)


# Q1
# age = int(input("enter age :"))
# cnic = input("do you have cnic (yes or no):")
# if age >= 18 and cnic == "yes" :
#     print("you are eligible to vote")
# else :
#     print("you are not eligible to vote")

# # debugging questions
# Q1
# x = 10
# y = 3
# print(x , y)

# Q3
# a = 5
# b = 10
# if a == b :
#     print("equal")

# Q3
# price = 500
# discount = 10
# final = price - price * discount / 100
# print(final)

# Q4
# x = 7 
# if x > 5 and x < 10 :
#    print("In range") 

# Q5

# items = ["pen", "book"] 
# if "pen" in items :
#     print("Found")
# else :
#     print("not found")


# items = [ "cpu" , "gpu" , "motherboard" ]
# new_item = input("enter a material :")
# if new_item in items : 
#     print(new_item,"aleady in cart")
# else :
#     print(new_item,"added to cart")

# mini assignment
# units_comsumed = int(input("number of units consumed :"))
# perunit_rate = 25
# due_date = input("duedate paseed or not (yes or no) :")

# total_bill = units_comsumed * perunit_rate
# if units_comsumed >= 300 :
#  units_comsumed *= 0.10
#  print(f"Your bill after surcharge is:{units_comsumed}")
# elif total_bill >= 5000 and due_date == "no" :
#     print("'Bill Overdue - Pay Immediately")
# else :
#    print("you can pay now or later")
# membership_category = input("enter category :").lower()
# membership = ["domestic", "commercial", "industrial"]   
# if membership_category in membership :
#    print("valid category")
# else :
#     print("invalid category")
# print(total_bill)

# Q
# Isaam = 5 + 3 * 2 ** 2
# print(Isaam)
# 5 + 3 * 4
# 5 + 12
# 17

# Q:
# expression = (5 + 3 * 2) > 10 and (10 % 3 == 1)
# print(expression)

# (5 + 6) > 10 and (10 % 3 == 1)
# 11 > 10 and (10 % 3 == 1)
# 11 > 10 and (1 == 1)
# True and (1 == 1)
# True and True
# True


# mini project
history = []
num1 = float(input("enter num1"))
num2 = float(input("enter num2"))
print(f"addition: = {num1 + num2}")
print(f"subtraction: = {num1 - num2}")
print(f"numtiplication: {num1 * num2}")
print(f"division: {num1 / num2}")
print(f"floor divison: {num1 // num2}")
print(f"modulus: {num1 % num2}")
print(f"exponent: {num1 ** num2}")

history.append {num1 , num2}
print(f"calculation history {history}")

if num1 > num2 :
    print("num1 is greater")
elif num1 == num2 : 
    print("both numbers are equal")
else :
    print("num2 is greater")



