#assignment 1
# Question 01
 #print statements
print("QUESTION 01")
print("Muhammad Isaam Muhammad Aslam")
print("maths")
print("i am learning python because it is very helpful for me and has demand in future")

#comments question 02
print("QUESTION 02")
name = "sara"  #creates a variable named name and stores text "sara" in it
age = 19 #creates a variable named age and stores number 19 in it
print("name") #displays the value stored in the variable name (sara) on screen
print(age) #displays the value stored in variable age (19) on screen

#rewrite
print("QUESTION 03")
"""
this program stores a person's name and age then prints them on the terminal
"""
#stores the text "sara" in the name variable
name = "sara"
#stores the number 19 in the age variable
age = 19
#displays the name on screen
print(name)
#displays the age on screen
print(age)

#variables and data types question 03
name = "m.isaam"
age = 13
height_in_feet = 4.11
city_you_live_in = "karachi"
is_student = True

print(name)
print(age)
print(height_in_feet)
print(is_student)

print(type(name))
print(type(age))
print(type(height_in_feet))
print(type(city_you_live_in))
print(type(is_student))

#type conversion(casting)
num1 = int("50")
num2 = 20
total = num1 + num2
print( "total is" , total)


#own short program
text_number = int("35")
result = text_number + 10
print( "the result is" , result)

#taking input from user
print("QUESTION 05")
name = input("enter your name")
age = int(input("enter your age")) 
next_age = age + 1
print("hello", name , " next year you will be" , next_age, "years old")

#operators
print("QUESTION 06")
#arithmatic operators
num1 = float(input("enter ur first number"))
num2 = float(input("enter ur second number"))

print( " sum " , num1 + num2)
print( " difference " , num1 - num2)
print( " divident " , num1 / num2)
print( " product " , num1 * num2)
print( " modulus " , num1 % num2)
print( " exponent " , num1 ** num2)
print( " floor division " , num1 // num2)

#comparision operators
num1 = float(input("enter ur first number: "))
num2 = float(input("enter ur second number: "))

print(" equal ", num1 == num2)
print(" not equal ", num1 != num2)
print(" greater than ", num1 > num2)
print(" less than ", num1 < num2)
print(" greater than or equal ", num1 >= num2)
print(" less than or equal ", num1 <= num2)

#logical operators
a = True
b = False

print(" and result ", a and b)
print(" or result ", a or b)
print(" not a result ", not a)
print(" not b result ", not b)

# assignment operators
x = 20
print(" initial x ", x)

x += 5
print(" after += ", x)

x -= 3
print(" after -= ", x)

x *= 2
print(" after *= ", x)

x /= 4
print(" after /= ", x)

#mini challenge simple bill calculator
print("QUESTION 07")
price = float(input("enter the price of the item"))
quantity = int(input("enter the quantity of the item"))
 
total_bill = price * quantity

if total_bill > 1000 :
    discount = total_bill * 0.10
    final_amount = total_bill - discount
    print(" you get a 10 percent discount. final amount to pay is :" , final_amount )
else:
    print("no discount applied. your final amount to pay is :" , total_bill )