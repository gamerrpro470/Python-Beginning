student_record = ("Ali", 101, 85, 90, 78)
print("Name:", student_record[0])
print("Roll Number:", student_record[1])
marks_tuple = student_record[2:]
print("Marks Sub-tuple:", marks_tuple)
average_marks = sum(marks_tuple) / len(marks_tuple)
print("Average Marks:", average_marks)
name, roll, m1, m2, m3 = student_record
print(name, roll, m1, m2, m3)
try:
    student_record[0] = "Ahmed"
except TypeError as e:
    print("Error (Immutable):", e)