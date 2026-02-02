# Variable naming rules in Python:
# must start with a letter or underscore
# can contain letters, numbers, and underscores 
# are case-sensitive
# cannot be a reserved keyword in Python

# name = "Naresh"
# _age = 30   
# _isStudent = False
# height_cm = 170.5
# print("Name:", name)

# basic data types: int, float, str, bool
# a, b, c, d = 3, 4.5, "Hello", True
# print("a:", a)
# print("b:", b)
# print("c:", c)
# print("d:", d)

# python decides the data type automatically
# print(type(a))      # int
# print(type(b))      # float     
# print(type(c))      # str
# print(type(d))      # bool

# user input input() function
# input is always taken as string
# user_name = input("Enter your name: ")

# typecasting - converting data types from one to another
# user_age = int(input("Enter your age: "))  # converting string input to int
# print("User Name:", user_name)
# print("User Age:", user_age)
# print("Type of user_age:", type(user_age))

"""bjkasdfg
afsdd fdas
fsdaa
fasd """  # multi-line comment / docstring

# + operator does concatenation for strings

# take two numbers as input and print their sum
# num1 = int(input("Enter first number, num1: "))  
# num2 = int(input("Enter second number, num2: "))
# sum = num1 + num2
# print("Sum:", sum)  


# arithmetic operators: + - * / % // **
a = 6
b = 3
print("a + b =", a + b)
print("a - b =", a - b)     
print("a * b =", a * b)
print("a / b =", a / b)      # float division
print("a // b =", a // b)    # floor division
print("a % b =", a % b)      # modulus
print("a ** b =", a ** b)    # exponentiation

# operator precedence: ** > * / % // > + - -

#q1. store your personal information using variables and print it
# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# address = input("Enter your address:")
# college = input("Enter your college name:")

# print("Name:", name)
# print("Age:", age)  
# print("Address:", address)
# print("College:", college)

#q2. Take two numbers and display their power
# num1 = int(input("Please enter first number, num1: "))
# num2 = int(input("Please enter second number, num2: "))
# print(num1**num2)

#q3. take radius as input and calculate area of circle
# radius = float(input("Please enter radius of circle: "))
# area = 3.14*radius**2
# print("The area of circcle is: ", area)

#q4. create diffrent variables and display their types
# x = 23
# y = 20.1
# z = True
# a = "Naresh"
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(a))

#q5.Take student name, age, marks in 5 subjects and calculate total and average
# name = input("Enter your name: ") 
# age = int(input("Enter your age: "))
# m1 = float(input("Enter marks of first subject, m1: "))
# m2 = float(input("Enter marks of first subject, m2: "))
# m3 = float(input("Enter marks of first subject, m3: "))
# m4 = float(input("Enter marks of first subject, m4: "))
# m5 = float(input("Enter marks of first subject, m5: "))

# total = m1+m2+m3+m4+m5;
# average = total/5
# print("your name: ", name)
# print("your age: ", age)
# print("Your total score is: ", total)
# print("Your average score is: ", average)


# string maipulation
# str1 = "Hello"
# str2 = "World"
# print(str1 + " " + str2)   # concatenation
# print(str1 * 3)            # repetition
# print("Length of str1:", len(str1))  # length of string
# print("Character at index 1 in str2:", str2[1])  # indexing
# print("Substring str1[1:4]:", str1[1:4])  # slicing
# print("Uppercase str1:", str1.upper())   # convert to uppercase
# print("Lowercase str2:", str2.lower())   # convert to lowercase
# print("Replace 'l' with 'x' in str1:", str1.replace('l', 'x'))  # replace substring
# print("Find 'o' in str2 at index:", str2.find('o'))  # find substring index
# print("Is str1 alphabetic?:", str1.isalpha())  # check if all characters are alphabetic
# print("Is str2 alphanumeric?:", str2.isalnum())  # check if all characters are alphanumeric
# print("Split str1 by 'e':", str1.split('e'))  # split string by delimiter

