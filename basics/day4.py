# Looping Statements in Python: for and while loops
# It is used to execute a block of code repeatedly until a certain condition is met.

# For Loop:
# The for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string). 
# Syntax:
# for item in sequence:
#     # do something with item  

# Example:
for i in range(1, 5):  # This will print numbers from 1 to 4
    print(i)

# another way to use for loop
# for i in range(1, 6):
#     print(f"Naresh - {i}")

# another way to use for loop 
# for i in range(1, 11, 2):  # This will print odd numbers from 1 to 10
#     print(i, end=" ")    

# for character in a string
for char in "Hello":
    print(char, end=" ")

print()  # for new line

str = "python"
for char in range(2, len(str)):
    print(str[char], end=" ") 


# Wap to check whether the number is prime or composite
# num = int(input("Please enter a number: "))
# if num > 1:
#     for i in range(2, int(num/2)+1):
#         if (num % i) == 0:
#             print(f"The number {num} is Composite")
#             break
#     else:
#         print(f"The number {num} is Prime")
# else:
#     print(f"The number {num} is neither Prime nor Composite")

# another way to check prime or composite
# num = int(input("Please enter a number: "))
# factor_count = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         factor_count += 1
# if factor_count == 2:
#     print(f"The number {num} is Prime")
# else:
#     print(f"The number {num} is Composite")

# While Loop:
# The while loop is used to execute a block of code as long as a specified condition is
# true.
# Syntax:
# while condition:
#     # do something

# Example:
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# use while loop to display even number from 2 to 20\
i = 2
while i <= 20:
    print(i, end=" ")
    i += 2

# wap to dispaly sum of n natural numbers
# n = int(input("Please enter a number: "))
# sum = 0
# i = 1
# while i<= n:
#     sum += i
#     i+=1
# print(f"the sum is: {sum}")

