# Coding Exercises
# Q1
for i in range(1, 11):
    print(i)
# Q2
count = 5
while count >= 1:
    print(count)
    count -= 1
# Q3
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
# Q4
for i in range(10, 101, 10):
    print(i)
# Q5
for i in range(1, 21):
    if i == 15:
        break
    print(i)
# Q6
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
# Q7
for i in range(1):
    pass


# Debugging Exercises
# Q1
for i in range(5):
    print(i)
# Q2
i = 1
while i <= 5:
    print(i)
    i += 1
# Q3
for i in range(1, 10):
    print(i)
# Q4
for i in range(5):
    if i == 3:
        break
    print(i)
# Q5
for i in range(5):
    if i == 2:
        continue
    print(i)



# Mini Assignment
for i in range(1, 6):
    print(i)
count = 5
while count >= 1:
    print(count)
    count -= 1
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(1, 21, 2):
    print(i)
for i in range(1, 10):
    if i == 7:
        break
    print(i)
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)


# Mini Project
num = int(input("Enter a number for the multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
for i in range(1, 11):
    for j in range(1, 6):
        print(f"{j}x{i}={j*i}", end="\t")
    print()
num = int(input("Enter a number for even multiples: "))
for i in range(2, 11, 2):
    print(f"{num} x {i} = {num * i}")
num = int(input("Enter a number (stops if result > 50): "))
for i in range(1, 11):
    result = num * i
    if result > 50:
        break
    print(f"{num} x {i} = {result}")
num = int(input("Enter a number (skips multiples of 3): "))
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(f"{num} x {i} = {num * i}")
if num > 0:
    pass

