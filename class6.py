# num1 = float(input("enter your number 1"))
# num2 = float(input("enter your number 2"))
# num3 = float(input("enter your number 3"))

# # # if num1 < num2 and num2 < num3 :
# #     print(f"the largest number is num3")
# # elif num1 < num3 and num3 < num2 :  
# #     print(f"the largest number is num2")
# # else:
#     print(f"the largest number is num1")


# if num1 > num2 and num1 > num3 :
#  print(f"the largest number is num1 ")
# elif num2 > num1 and num2> num3 :
#  print("the largets number is num2 ")
# else :
#  print("the largest number is num3 ") 


#atm machine
current_balance = 10000
withdraw_amount = float(input("enter amount to withdraw"))
if withdraw_amount <= current_balance:
 print("withdraw successful")
else : 
 print("withdraw unsuccessful, insufficiant balance")

current_balance -= withdraw_amount
print(f"after withdrawing your amount {withdraw_amount} now your current balance is {current_balance}")

 


