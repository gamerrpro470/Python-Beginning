#coding exercises

# Q24
print("isaam")
print("python course")

# Q25
age = 13
print(age)

# Q26
num1 = 17
num2 = 1002
sum = num1 + num2
print(sum)

# Q27
name = (input("enter your name"))
age = int(input("enter your age"))
print(f"your name is {name} and your age is {age}")

# Q28
a = 19
b = 31
a, b = b,a
print(a ,b)

# Q29
num1 = int(input("enter your number"))
num2 = int(input("enter your number"))
sum = num1 + num2
print(sum)

# Q30
name = "isaam"
print(type(name))

# Q31
print( " isaam " , " ali " , " ahmed " , sep = " * " , end = " list of students" )


#debugging questions

# debug1
print("Hello World")

# debug2
name = input("enter name :")
print(name)

# debug3
name = "Ali"
print("name")

# debug4
num = 10
print("num")

# debug5
age = int(input("enter age : "))
print(f"your age is {age}")

# mini assignment
name = input("enter your name:")
age = int(input("ener your age:"))
favourite_subject = input("whats your favourite subject:")
age_after_five_years = "age" + 5
print("age_after_five_years")
print(type(name))
print(type(age))
print(type(favourite_subject))
print(f"Hi {name} you are {age} years old and your favourite subject is {favourite_subject} and after five years your age will be {age_after_five_years}")
# first of all i took input from user his name age and his fav subject then in the 67th line i made a variable in which i made a command of addition to tell user his or her age after 5 years then i printed the data type of the name age and fav subject then printed the users name age fav subject and age after 5 years in a single sentence using f concatination method.


# mini project
name = input("enter name :")
age = int(input("enter age :"))
profession = input("what is your profession :")
country = input("enter your country name :")
current_year = 2026
approx_birthyear = current_year - age
current_rank = "diamond"
target_rank = "elite_master"
current_rank , target_rank = target_rank , current_rank
print("PERSONAL_ID")
print (f"| name | : {name} * | Profession | : {profession} *")
print (f"| age | : {age} * | birth year | : {approx_birthyear} *")
print (f" | current renk | : {current_rank} * | target rank | : {target_rank} *")
print (f" | country | : {country} *")
