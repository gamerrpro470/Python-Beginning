# Conditional Statement
# coding exercises

# Q1
# number = float(input("enter a number :"))
# if number >= 100:
#     print("number is equal to or greater than 100 ")
# else :
#     print("number is smaller than 100")

# Q2
#  student_marks = float(input("enter your marks :"))
#  if student_marks >= 40 and student_marks < 101:
#      print("you have passed the exam")
#  elif student_marks < 40 :
#      print("you have failed the exam")
#  elif student_marks > 101 :
#    print("invalid marks")

# Q3
marks = float(input("enter your marks :"))
if marks > 80 and marks < 101:
    print("you have got grade 'A'")
elif marks >= 61 and marks <= 80:
    print("you have got grade 'B'")
elif marks >= 41 and marks <= 60:
    print("you have got grade 'C'")
elif marks >= 0 and marks <= 40:
    print("you have got grade 'F'")
else:
    print("invalid marks")

# Q4
age = int(input("Enter your age: "))
if age >= 18:
    has_id = input("Do you have an ID card? (yes/no): ").lower()
    if has_id == "yes":
        print("Entry Allowed")
    else:
        print("Entry Denied, ID card is required.")
else:
    print("Entry Denied, You are underage.")

# Q5
num = int(input("Enter a number: "))
result = "The number is zero." if num == 0 else "The number is not zero."
print(result)

# Q6
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print(f"The largest number is {largest}.")

# Q7
correct_username = "staff"
correct_password = "095123"
username = input("Enter username: ")
if username == correct_username:
    password = input("Enter password: ")
    if password == correct_password:
        print("Login Successful")
    else:
        print("Login Failed, Incorrect password.")
else:
    print("Login Failed, Username not found.")

# Q8
year = int(input("Enter a year: "))
result = "Leap Year" if year % 4 == 0 else "Not a Leap Year"
print(result)

# debugging exercises
# debug1
# sol
x = 10
if x > 5:
    print("Big")

# debug2
# sol
age = 20
if age >= 18:
    print("Adult")

# debug3
# sol
marks = 80
if marks >= 90:
    print("A")
elif marks >= 70:
    print("B")

# debug4
# sol
num = 6
if num > 0:
    if num % 2 == 0:
        print("Positive Even")

# debug5
# sol
age = 16
status = "Adult" if age >= 18 else "Minor"

# mini assignment
num = float(input("Enter a number: "))
if num > 0:
    sign = "Positive"
elif num < 0:
    sign = "Negative"
else:
    sign = "Zero"
even_odd = "N/A"
if num > 0:
    if num % 2 == 0:
        even_odd = "Even"
    else:
        even_odd = "Odd"
status = "Zero" if num == 0 else "Non-Zero"
print(f"\n--- Program Developed by Me ---")
print(f"Number Sign: {sign}")
print(f"Even/Odd Status: {even_odd}")
print(f"Zero Status: {status}")

# mini project
name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))
if marks < 0 or marks > 100:
    print("Error: Invalid input! Marks must be between 0 and 100.")
else:
    if marks >= 90:
        grade = "A"
        if marks >= 95:
            grade += " (Distinction)"
    elif marks >= 70:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "F"
    status = "Pass" if marks >= 50 else "Fail"
    print(f"\n==============================")
    print(f"       STUDENT REPORT         ")
    print(f"      Created by: Me          ")
    print(f"==============================")
    print(f"Student Name : {name}")
    print(f"Marks Obtained: {marks}/100")
    print(f"Final Grade   : {grade}")
    print(f"Status        : {status}")
    print(f"==============================")


