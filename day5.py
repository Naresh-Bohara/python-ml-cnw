# Control flow statements in Python
# break, continue, pass

# Example of break statement
# for i in range(10):
#     if i == 5:
#         break  # Exit the loop when i is 5
#     print(i, end=' ')
# print()
# print("Loop ended using break statement.")

#q1. print first 5 even numbers (1, 20) using break statement
# count = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i, end=' ')
#         count += 1
#     if count == 5:
#         break
# print()

# continue: skips the current iteration and move to next iteration
# loop doesn't stop, only current value is ignored.
# for i in range(1, 6):
#     if i ==3:
#         continue
#     print(i, end=" ")

# pass: placeholder
# for i in range(1, 6):
#     pass



#q. reverse a number : 123---output: 321
# num = int(input("Please enter a multi-digit number to reverse: "))
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10
# print("Reversed number:", rev)

# for num in range(1, 11):
#     if num == 3:
#         continue
#     for i in range(1, 11):
#         print(f"{num} X {i} = {num*i}")
# print()

