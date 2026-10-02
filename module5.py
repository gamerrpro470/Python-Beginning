# coding exercises

# Q1
name = input("enter your name: ")
print(f"upper case: {name.upper()}")
print(f"lower case: {name.lower()}")
print(f"title case: {name.title()}")

# Q2
language = "python"
print(language[::-1])


# Q3
sentence = "i love python because python is easy to learn."
word_to_count = "python"
count = sentence.count(word_to_count)
print(f"the word '{word_to_count}' appears {count} times in the sentence.")

# Q4
email = input("enter your email:")
if "@" in email:
    print("valid email")
else:
    print("invalid email")

# Q5
sentence = "python is a programming language. python is widely used in web development, data science, and automation."
print(sentence.split())
print(" ".join(sentence))

# Q6
word = ("                  python                            ")
print(word.strip())

# Q7
input = input("enter anything :")
print(input.isdigit())

# Q8
name = input("enter name:")
age = int("enter age:")
print(f"hello {name} your age is {age}")

# debugging exercises
# Q1
s = 'Python' 
print(s[4]) 

# Q2
s = "hello" 
print(s.upper())

# Q3
name = "Ali" 
age = 20 
print("Name: " + name + " Age: " + str(age))

# Q4
words = ["I", "love", "Python"] 
print(" ".join(words))

# Q5
s = ("  Hello  ") 
print(s.strip())








