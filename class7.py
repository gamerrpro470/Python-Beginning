#nasted if else

#program eligible to vote
# name = (input("enter your name"))
# age = int(input("enter your age"))
# nationality = input("enter your nationality")
# if nationality == "Pakistani" and age >= 18 :
#     print(f"hello {name} you are eligible to vote")
# elif age < 1 or age > 150:
#     print("invalid age")
# else:
#     print(f"hello {name} you are not eligible to vote")


#bill calculator
# bill = float(input("enter your total bill"))
# if bill >= 5000:
#     print("20% discount applied")
#     discount = bill * 0.20
#     final_bill = bill-discount
#     print(f"your final bill after discount is {final_bill}")
# elif bill >=2000 and bill < 5000: 
#     print("10% discount applied")
#     discount = bill * 0.10
#     final_bill = bill - discount
#     print(f"your final bill after discount is {final_bill}")
# else:
#     print(f"no discount applied , your final bill is {bill}")


# forloop
# for i in range (1 , 21):
#     print(i)

# #multiplication table
# number = int(input("enter your number"))
# for i in range (1 , 13):
#     print(f"{number}  x {i} = {number*i}")

# SUM OF FIRST 100 NUMBERS

total = 0
for i in range ( 1 , 101):
  total = total + i
print(f" " )