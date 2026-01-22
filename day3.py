# accessing characters in a string by index
# str1 = "Programming"
# print("Character at index 0:", str1[0])  # First character

# f-string formatting to include variables in a string
# name = "Naresh"
# age = 25
# # old method 
# print("My name is %s and I am %d years old." % (name, age))

# # anothere way 
# print("My name is " + name + " and I am " + str(age) + " years old.")

# # another way 
# print("My name is", name, "and I am", age, "years old.")

# # old method
# print("My name is {} and I am {} years old.".format(name, age))

# # another way 
# print("My name is {0} and I am {1} years old.".format(name, age))

# # new method
# print(f"My name is {name} and I am {age} years old.")

# # Using f-strings for formatted output  
# # take a sting input and display its first and last character
# word = input("Please enter a word: ")
# print (f"First character: {word[0]}, Last character: {word[-1]}")

# # another way for last character
# print("Last character:", word[len(word)-1])


# Conditional statements if, elif, else, nested if, pass statement

# if : single statement
# syntax:
# if condition:
#     # code to be executed if condition is true
# age = int(input("Please enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")

# if-else : two statements
# syntax:
# if condition:
#     # code to be executed if condition is true
# else:
#     # code to be executed if condition is false
# age = int(input("Please enter your age: "))
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# if-elif-else : multiple statements
# syntax:
# if condition1:
#     # code to be executed if condition1 is true
# elif condition2:
#     # code to be executed if condition2 is true
# else:
#     # code to be executed if both conditions are false
# marks = int(input("Please enter your marks: "))
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 75:
#     print("Grade: B")
# elif marks >= 60:
#     print("Grade: C")
# elif marks >= 40:
#     print("Grade: D")
# else:
#     print("Grade: F")

# nested if : if statement inside another if statement
# syntax:
# if condition1:
#     if condition2:
#         # code to be executed if both conditions are true
#     else:
#         # code to be executed if condition1 is true and condition2 is false
# else:
#     # code to be executed if condition1 is false
# num = int(input("Please enter a number: "))
# if num >= 0:
#     if num == 0:
#         print("The number is zero.")
#     else:
#         print("The number is positive.")
# else:
#     print("The number is negative.")
# pass statement : used as a placeholder for future code
# syntax:
# if condition:
#     pass
# else:
#     # code to be executed if condition is false
# num = int(input("Please enter a number: "))
# if num >= 0:
#     pass  # Placeholder for future code
# else:
#     print("The number is negative.")



# if:
# age =14
# if age >= 13:
#     print("owoo")

#q1. WAP  to check if number is greater then 10
# number = int(input("Please Enter a Number: "))
# if number > 10:
#     print("Yes, the number you entered is greater then 10.")

#q2. WAP to check whether number is positive or negative
# number = int(input("Please Enter a Number: "))
# if number > 0:
#     print("The number is positive")
# else: 
#     print("The number is negative")

#q3. WAP to enter age and display "Child " if age <13, "teen" if age <20, and "adult" otherwise
# age = int(input("Enter your age: "))
# if age <13:
#     print("You are a child")
# elif age <20:
#     print("You are a teen")
# else:
#     print("You are adult")

#q4. WAP to enter traffic light color and display appropriate message: Red: Stop, Yellow: Get ready, Green: Go
light_color = input("Please enter color signal red, yellow, or green: ")
if light_color == "red":
    print("Please stop! ")
elif light_color == "yellow":
    print("Get ready!")
elif light_color == "green":
    print("Please Go!")
else:
    print("Please enter valid signal color!")


# Comparison operators and arithmetic operators
# comparison operators: ==, !=, >, <, >=, <=
# == : equal to
# != : not equal to
# >  : greater than
# <  : less than
# >= : greater than or equal to
# <= : less than or equal to

a = 12
b = 7
print("a == b:", a == b)   # False
print("a != b:", a != b)   # True
print("a > b:", a > b)     # True
print("a < b:", a < b)     # False
print("a >= b:", a >= b)   # True
print("a <= b:", a <= b)   # False

 # logical operators: and, or, not
 # and : returns True if both operands are true
 # or  : returns True if at least one operand is true
 # not : returns True if operand is false

# only citizens above 18 years and having voter ID are eligible to vote
age = int(input("Please enter your age: "))
has_voter_id = input("Do you have a voter ID? (yes/no): ").lower() == "yes"
if age >= 18 and has_voter_id:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# only one condition should be true
# citizen above 65 years or having special disability can avail senior citizen benefits 
age = int(input("Please enter your age: "))
has_disability = input("Do you have a special disability? (yes/no): ").lower() == "yes"
if age > 65 or has_disability:
    print("You can avail senior citizen benefits.")
else:
    print("You are not eligible for senior citizen benefits.")

# not operator example
is_raining = input("Is it raining? (yes/no): ").lower() == "yes"
if not is_raining:
    print("You can go for a walk.")
else:
    print("Better to stay indoors.")

