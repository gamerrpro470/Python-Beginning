# Coding Exercises

# Q26
cities = ["Karachi", "Lahore", "Islamabad", "Faisalabad", "Multan"]
print(cities)

# Q27
numbers = [10, 20, 30, 40, 50]
print(numbers[0], numbers[-1])

# Q28
items = ["A", "B", "C", "D", "E", "F", "G"]
print(items[2:5])

# Q29
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])

# Q30
fruits = ["apple", "banana"]
fruits.append("orange")
fruits.insert(1, "mango")
fruits.remove("banana")
print(fruits)

# Q31
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numbers)

# Q32
scores = [10, 20, 30, 40, 50]
total_sum = 0
for score in scores:
    total_sum += score
average = total_sum / len(scores)
print(total_sum, average)

# Q33
data = [40, 10, 30, 20]
data.sort()
print(data)
data.reverse()
print(data)


# Debugging Exercises

# Debug 1:
fruits = ["apple", "banana"]
fruits.append("mango")

# Debug 2:
nums = [1, 2, 3]
print(nums[2])

# Debug 3:
a = [1, 2, 3]
if 5 in a:
    a.remove(5)

# Debug 4:
lst = [3, 1, 2]
result = sorted(lst)
print(result)

# Debug 5:
nums = [1, 2, 3]
for n in nums.copy():
    nums.append(n)


# Mini Assignment
marks = []
marks.append(78)
marks.append(45)
marks.append(92)
marks.append(55)
marks.append(38)
marks.sort()
print("Sorted Marks:", marks)
lowest_marks = marks[0]
highest_marks = marks[-1]
print("Lowest Marks:", lowest_marks)
print("Highest Marks:", highest_marks)
above_50 = [m for m in marks if m > 50]
print("Marks above 50:", above_50)
average_marks = sum(marks) / len(marks)
print("Average Marks:", average_marks)


# Mini Project
contacts = []
name1 = input("Enter name: ")
phone1 = input("Enter phone number: ")
contacts.append([name1, phone1])
print("\n--- Contact List ---")
for contact in contacts:
    print(f"Name: {contact[0]}, Phone: {contact[1]}")
search_name = input("\nEnter name to search: ")
found = False
for contact in contacts:
    if contact[0].lower() == search_name.lower():
        print(f"Number found: {contact[1]}")
        found = True
        break
if not found:
    print("Contact not found.")
delete_name = input("\nEnter name to delete: ")
for contact in contacts:
    if contact[0].lower() == delete_name.lower():
        contacts.remove(contact)
        print("Contact deleted successfully.")
        break
contacts.sort(key=lambda x: x[0])
print("\nSorted Contacts:", contacts)
pakistani_numbers = [c for c in contacts if c[1].startswith('03')]
print("\nNumbers starting with '03':", pakistani_numbers)

