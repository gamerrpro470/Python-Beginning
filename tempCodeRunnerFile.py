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