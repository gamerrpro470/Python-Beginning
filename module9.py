# # dictionary

# # coding exercises
# # Q1
# new_fruits = { "watermelon" : 150 , "raspberry" : 350 , "kiwi" : 400 }
# print(new_fruits)

# # Q2
# new_fruits["avocado"] = 300
# new_fruits["kiwi"] = 250
# print(new_fruits)

# # Q3
# print(new_fruits.get("grapes"))

# # Q4
# print(new_fruits.keys())
# print(new_fruits.values())

# # Q5
# for fruits in new_fruits :
#     print(new_fruits.items()) 

# for keys , values in new_fruits.items():
#     print(f"{keys} -->> {values}")

# new_fruits.update({"grapes" : 200 , "lechee" : 300})
# print(new_fruits)

# deleting_value = new_fruits.pop("lechee")
# print(new_fruits)
# print(deleting_value)

# Q
# football_players = { "Spain" : "lamine Yamal" , "Portugal" : "Cristiano Ronaldo" , "France" : "Kylian Mbappé" , "Argentina" : "Lionel Messi" }
# print(football_players["Portugal"])

# debugging_exercises
# debug1 :
# student = {"name" = "Ali", "age": 20}
# print(student)

# student = {"name" : "Ali", "age": 20}
# print(student)

# debug2 :
# student = {"name": "Ali"}
# print(student["age"])

# student = {"name": "Ali"}
# print(student.get("age")) 

# debug3 :
# student = {"name": "Ali", "age": 20}
# keys = student.keys()
# print(keys[0])

# student = {"name": "Ali", "age": 20}
# keys = student.keys()
# print(keys)

# debug4 :
# student = {}
# item = student.popitem()

# student = {"name": "Ali", "age": 20}
# item = student.popitem()
# print(student)

# debug5 :
# student = {"name": "Ali", "age": 20}
# for k in student.values():
#  print(k, student[k])

# Q7

# Data = {
#     "student1": {"name": "Ali", "age": 20},
#     "student2": {"name": "Ahmed", "age": 22}
#        }
# print(Data["student1"]["name"])
# print(Data["student2"]["name"])

# Q8
# dictionary = { "rtx 4090" : 800000 , "rtx 4080" : 650000 , "rtx 4070" : 500000 }
# dictionary.clear()
# print(dictionary)


# Mini Assignment
# employee = { "name" : "ahmed" , "department" : "IT" , "salary" : 80000 }
# bonus_value = employee.get("bonus" , 0 )
# employee.update({"salary" : 90000 , "experience" : "4 years"})
# for keys , values in employee.items():
#     print(f"{keys} : {values}")
# removing_value = employee.pop("experience")
# print(employee)

# Mini Project
students = { "roll_no1" : {"name" : "Ali" , "age" : 20 , "marks" : 80} ,
             "roll_no2" : {"name" : "Ahmed" , "age" : 22 , "marks" : 90} ,
             "roll_no3" : {"name" : "Abdullah" , "age" : 21 , "marks" : 85} 
            }
print(f"taking_input_from_user \n")

roll_no = input("Enter the roll number :")
name = input("Enter the name :")
age = int(input("Enter the age :"))
marks = int(input("Enter the marks :"))

print(f"updating_the_dictionary\n")
students.update({roll_no: {"name" : name , "age" : age , "marks" : marks}})
print(students)

print(f"searching_the_dictionary\n")
roll_number = input("Enter the roll number to see details :")
if roll_number in students:
    print(students[roll_number])
elif roll_number not in students:
    print("roll number not found")
else:
    print("invalid roll number")
print(f"updating_the_dictionary\n")
updating_marks = input("Enter the roll number to update marks :")
if updating_marks in students:
    update_marks = input("Enter the new marks :")
    students[updating_marks].update({"marks" : update_marks})
    print(students[updating_marks])
else :
    print("roll number was not found")
for keys , values in students.items():
    print(f"{keys} --> {values}")
students.pop("roll_no2")
print(students)





