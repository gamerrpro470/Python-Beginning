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



