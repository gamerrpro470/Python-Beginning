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
dictionary = { "rtx 4090" : 800000 , "rtx 4080" : 650000 , "rtx 4070" : 500000 }
dictionary.clear()
print(dictionary)








































