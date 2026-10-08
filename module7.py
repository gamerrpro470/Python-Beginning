# Coding Exercises
# 1
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print(fruits)
# 2
print("First:", fruits[0])
print("Last:", fruits[-1])
# 3
print("Middle 2:", fruits[1:3])
# 4
numbers = (1, 2, 3, 2, 4, 2, 5)
print("Count of 2:", numbers.count(2))
# 5
packed_tuple = ("Karachi", 2026, True)
city, year, status = packed_tuple
print(city, year, status)
# 6
a = 10
b = 20
a, b = b, a
print("a:", a, "b:", b)
# 7
mixed_tuple = ([1, 2, 3], "test")
mixed_tuple[0].append(4)
print(mixed_tuple)
# 8
try:
    fruits[0] = "mango"
except TypeError as e:
    print("Error observed:", e)


# debugging Exercises

# Debug 1:
t = [1, 2, 3]
t[0] = 10

# Debug 2:
single = (5,)
print(type(single))

# Debug 3:
t = (1, 2, 3)
if 5 in t:
    print(t.index(5))

# Debug 4:
a, b, c = (1, 2, 3)
print(a, b, c)

# Debug 5:
t = (1, 2, 3)
print(t[2])


# Mini Assignment
subjects = ("Maths", "Physics", "Chemistry", "English", "Maths")
print("First subject:", subjects[0])
print("Last 3 subjects:", subjects[-3:])
print("Is Physics in tuple?", "Physics" in subjects)
print("Occurrences of Maths:", subjects.count("Maths"))
sub1, sub2, sub3, sub4, sub5 = subjects
print(sub1, sub2, sub3, sub4, sub5)


# Mini Project
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
