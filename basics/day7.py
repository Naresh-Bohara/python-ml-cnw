### Searching:

# data = [
#     ["Ram", 24, "KTM"],
#     ["Shyam", 22, "Pokhara"],
#     ["Naresh", 23, "Dhangadhi"],
#     ["Hem", 25, "Pokhara"],
# ]

# target_name = input("Please enter the name to be searched: ").lower()
# target_address = input("Please enter the address to be searched: ").lower()
# print()

# found = False

# for item in data:
#     item_name = str(item[0]).lower()
#     item_address = str(item[2]).lower()

#     if item_name == target_name or item_address == target_address:
#         print(f"Found record: Name: {item[0]}, Age: {item[1]}, Address: {item[2]}")
#         found = True
# if not found:
#     print("No matching record found.")



### List Comprehension:
## normal way
# list of square of numbers from 1-5
# square_numbers = []
# for i in range(1, 6):
#     square_numbers.append(i*i)
# print(square_numbers)

# List Comprehension:
# syntax:
# new_list = [expression for item in iterable]
# square_numbers = [i*i for i in range(1, 6)]
# print(square_numbers)

# if list is given 
# numbers = [1, 2, 3, 4, 5, 6]
# square_numbers = [i*i for i in numbers if i % 2 == 0]
# print(square_numbers)

# normal way 
# even = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         even.append(i)

# print("Even numbers:", even)

# List Comprehension:
# syntax: new_list = [expression for item in iterable if condition]
# even = [i for i in range(1, 11) if i % 2 == 0]
# print("Even numbers:", even)


# ### Print value in uppercase:
# fruits = ["apple", "mango", "orange"]
# new_list = [fruit.upper() for fruit in fruits]
# print(new_list)


'''
input = [1,2,3,4,5]
output = ['odd', 'even', 'odd', 'even', 'odd']
'''

# input_list = [1, 2, 3, 4, 5]
# result = ["even" if i % 2 == 0 else "odd" for i in input_list]
# print(result)


word = ["madam", "hello", "lol", "level", "radar"]
palindrome = [i for i in word if i[::-1] == i]
print(palindrome)