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
counter = 91
def updatecounter():

    global counter
    counter += 3
updatecounter()
print(counter)

    


