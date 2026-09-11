# function
# coding exercises

# Q1
# def average(num1, num2):
#     return(num1 + num2) /2
# print(average(100, 20))
# or
# result = average(100, 20)
# print(result)

# Q2
# def student(name = "isaam"):
#     print("hello",name)

# student()
# # or
# student = "ahmad"

# Q3
# def max_number(*number):
#     max_num = max(number)
#     print(max_num)

# max_number(10, 70 , 30, 50, 90)

# Q4
# def student_info(**details):
#     print(details)

# student_info(name = "Isaam" , age = 14 , country = "Pakistan" )

# Q5
# cube = lambda a: a ** 3
# print(cube(4))

# Q6
# def recursive_sum(n):
#     if n <= 1:
#         return n

#     return n + recursive_sum(n - 1)
# print(recursive_sum(5))  

# Q7
# counter = 91
# def updatecounter():

#     global counter
#     counter += 3
# updatecounter()
# print(counter)

# debugging questions
# Q1
# def greet():
#      print("Hello")
#      greet()

# def greet():
#     print("hello")

# greet()

# Q2
# def add(a, b):
#       return a + b
#
# print(add(5)) 

# def add(a, b):
#          return a + b

# print(add(5, 2)) 

# Q3
# def square(n)
#      return n * n

# print(square(4)) 

# def square(n):
#      return n * n

# print(square(4)) 

# Q4
# def total(*args):
#          print(args + 1)

# total(1, 2, 3) 

# def total(*args):
#           print(args, 1)

# total(1, 2, 3)

# Q5
# def show():
#          print(x)
#          x = 10

# show() 

# def show():
#          x = 10
#          print(x)

# show() 

# mini assignment
# def student_marks(subject1 = 0, subject2 = 0 , subject3 = 0):
#     total = subject1 + subject2 + subject3
#     print(total)
#     average = total / 3
#     print(average)
#     grade = lambda average: "A" if average >= 80 else "B" if average >= 60 else "C" if average >= 40 else "Fail"
#     print("Grade", grade(average))
# student_marks(100, 90, 80)

# mini project
def sum(a , b):
    return a + b 

# add = sum(12 , 4)

def minus(a , b):
    return a - b

# subtract = minus(10 - 7)

def multiplication(a , b):
    return a * b

# multiply = multiplication(12 , 4)

def division(a , b = 1):
    return a / b

# divide = division(12 / 2)

def operations(*args):
    return sum(args)

average = lambda a , b : (a + b) / 2

def factorial(n):
    if n == 0 :
        return 0
    return n * factorial(n -1)


