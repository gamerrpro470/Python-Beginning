# Q1
name = input("enter your name :")
course = input("enter your course name :")
university = input("enter your university name :")
semester = int(input("enter your semester :"))
city = input("enter your city name:")
print(f"my name is {name} and my course is {course} i study in {university} and im on {semester} and i live in {city}")

# Q2
day = int(input("whats the day :"))
month = input("whats the month :")
year = input("whats the year :")
print(str(day) + "month" + str(year))

# Q3
item_name =input("enter item name :")
quantity = int(input("enter quantity :"))
price = float(input("enter price :"))
print(f"{quantity} x {item_name} = {price} ")

# Q3
temperature = input("enter temperature :")
print(f"todays temperature is {temperature}")

# Q4
length = float(input("enter length :"))
width = float(input("enter width :"))
area = length * width
print(f"area is {area}")

# Q5
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")
combined_word = word1 + word2
print("Combined word:", combined_word)

# Q6
name = input("enter your name :")
age = int(input("enter your age :"))
physics = int(input("enter physics marks :"))
chemistry = int(input("enter chemistry marks :"))
biology = int(input("enter biology marks :"))
total_fee = int(input("enter total fee :"))
subject_marks_total = physics + chemistry + biology
average = subject_marks_total / 3
if age <= 18 :
    print("underage")
else :
    print("overage")
if average <= 50 :
    print("pass")
else :
    print("fail")

print(f"student name is {name} and his age is {age} and he is enrolled in physics , chemistry , and biology")
print(f"{physics} + {chemistry} + {biology} = {subject_marks_total} , Average = {average}")
discount = total_fee * 0.10
discounted_fee = total_fee - discount
print(f"{discounted_fee}")
