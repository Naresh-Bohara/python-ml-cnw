# ### ---------------------- Assignment day-6 ----------------------------------

# #q1. WAP to create list of 5 fruits and display it
# fruits = []
# print("Enter the fruits below: ")
# for i in range(5):
#     fruit = input(f"Enter fruit {i+1}: ")
#     fruits.append(fruit)
# print(fruits)

# #q2. WAP to print the first and last element of list
# students = []
# size = int(input("Please enter the size no. of students: "))
# for i in range(size):
#     student = input(f"Enter the name of student-{i+1}: ")
#     students.append(student)
# print("Students list: ",students)

# if size>0:
#     print(f"First element: {students[0]}")
#     print(f"Last element: {students[-1]}")
# else:
#     print("Student List is empty.")

# q3. WAP to take 5 numbers from user and store in list
# numbers = []
# print("Enter the numbers below: ")
# for i in range(5):
#     num = int(input(f"Enter number-{i+1}: "))
#     numbers.append(num)
# print(numbers)

# numbers = []
# for i in range(5):
#     numbers.append(int(input(f"Enter number-{i+1}: ")))
# print(numbers)

# #q4. WAP to add one element at 2nd position of list
# subjects = []
# sub_size = int(input("Please enter the no.of subjects: "))
# for i in range((sub_size)):
#     sub = input(f"Please enter subject-{i+1}: ")
#     subjects.append(sub)
# print(subjects)

# print("inserting at 2nd index: ")
# subjects.insert(1, "biology")
# print(subjects)

# #q5. WAP to remove an element from list
# countries = []
# country_size = int(input("Enter the no.of countries: "))
# for i in range(country_size):
#     countries.append(input(f"Enter country-{i+1}: ").lower())
# print(f"Original countries: {countries}")
# print()
# remove_country = input("Enter the country to remove: ")
# if remove_country in countries:
#     countries.remove(remove_country)
#     print("Updated countries: ", countries)
# else:
#     print("Country not Found.")

# #q6. WAP to sort list in descending order
# products = []
# product_size = int(input("Enter the no. of products: "))
# for i in range(product_size):
#     products.append(input(f"Enter the product-{i+1}: ").lower())
# print(f"Original products order: {products}")
# print()
# products.sort(reverse=True)
# print("Products in descending order: ", products)

# #q7. WAP to reverse a list using slicing
# names = ["naresh", "shyam", "rohan", "abishek", "santosh", "hem"]
# print(names)
# reversed_names = names[::-1]
# print(reversed_names)

# #q8. WAP to store at least 20 numbers in list and print only even numbers
# numbers = []
# num_size = int(input("Please enter the no. of elements: "))
# for i in range(num_size):
#     num = int(input(f"Please enter num-{i+1}: "))
#     if num % 2 ==0:
#         numbers.append(num)
# print(numbers)

# #q9. WAP to store at least 20 numbers in list and print only odd numbers
# numbers = []
# num_size = int(input("Please enter the no. of elements: "))
# for i in range(num_size):
#     num = int(input(f"Please enter num-{i+1}: "))
#     if num % 2 != 0:
#         numbers.append(num)
# print(numbers)

# #q10. WAP to program to find largest number in list
numbers = []
num_size = int(input("Please eneter the no. of elements: "))
for i in range(num_size):
    numbers.append(int(input(f"Enter num-{i+1}: ")))
print(numbers)

# print(max(numbers))

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"The largest element in list is: {largest}")