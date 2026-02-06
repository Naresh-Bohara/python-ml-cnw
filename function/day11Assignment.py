# -------------------------- Day-11 Assignment -----------------------------

# q1. Program to take sentence from user and split it into word and print it
sentence = input("Please enter a sentence: ")
words = sentence.split()
print("Words in the sentence are:")
for word in words:
    print(word)

# q2. program to take sentence from user and count how many times a certain letter appears in it
sentence = input("Please enter a sentence: ")
letter = input("Enter a letter to count: ")
count = sentence.count(letter)
print(f"The letter '{letter}' appears {count} times")


# q3. program to take gmail from user, print valid if it ends with @gmail.com, invalid if not
email = input("Pleae enter your email: ")
if email.endswith("@gmail.com"):
    print("Valid Gmail")
else:
    print("Invalid Gmail")


# q4. program to take sentence from user and count total number of word and total number of character
sentence = input("Please enter a sentence: ")

words = sentence.split()
word_count = len(words)
char_count = len(sentence)

print("Total number of words:", word_count)
print("Total number of characters:", char_count)
