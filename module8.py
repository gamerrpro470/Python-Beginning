# module 8

# Mini Assignment
name = input("Enter your full name: ")
formatted_name = name.title()
print(f"Formatted Name: {formatted_name}")
length = len(name)
print(f"Total length of name: {length}")
if ' ' in name:
    print("Yes, there is a space in the name.")
else:
    print("No, there is no space in the name.")
reversed_name = name[::-1]
print(f"Reversed Name: {reversed_name}")

# Mini Project
sentence = input("Enter any sentence: ")
words = sentence.split()
total_words = len(words)
print(f"Total word count: {total_words}")
letter = input("Enter a specific letter to count: ")
letter_count = sentence.count(letter)
print(f"The letter '{letter}' appears {letter_count} times.")
print(f"Upper Case: {sentence.upper()}")
print(f"Lower Case: {sentence.lower()}")
print(f"Title Case: {sentence.title()}")
word_to_find = input("Enter a word to search for: ")
if word_to_find in sentence:
    print(f"Yes, the word '{word_to_find}' is present in the sentence.")
else:
    print(f"No, the word '{word_to_find}' is not present in the sentence.")
reversed_sentence = sentence[::-1]
print(f"Reversed Sentence: {reversed_sentence}")
