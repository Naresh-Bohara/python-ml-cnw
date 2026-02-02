## Sequence data types in python:
# These data types store multiple values in one variable. 
# List, Tuple, Dictionary, Set

# List: it is a collection of items which is ordered, changeable(mutable), and allows duplicate values
# myList = [10, 20, 30, 40]
# fruits = ["apple", "banana", "orange", "mango", "apple"]
# print(fruits)

# multiList = [
#     ["apple", "banana", "orange", "mango"], 
#     ["dog", "cat", "elephant", "lion"]
# ]

# # Properties
# print(myList[0])
# print(fruits[0])
# print(multiList[1][0])

## Method of List:
# append(), insert(), remove(), pop(), sort(), reverse(), length(), clear(), count(), index(), extend(), copy(), join(), slice(), min(), max(), sum(), etc.

num = [1, 2, 3, 4, 5, 3, 2, 1, 1]

# fruits = ["apple", "banana", "orange", "mango", "apple"]

# num.append(6)
# print(num)                   # add item in the last index

# num.insert(1, 0)             # add item at given index
# print(num)

# num.remove(2)                # remove given item
# print(num)

# popped_value = num.pop()     # remove item at given index, if not given then remove last item
# print(popped_value)
# print(num)

# num.sort(reverse=True)        # sort in decending
# print(num)
# num.sort()                    # sort in ascending
# print(num)

# num.reverse()                 # reverse list
# print(num)

# print(len(num))               # length of list      
# num.clear()                   # clear all items in list
# print(num)

# print(fruits.count("apple")) # count occurrence of item

# print(fruits.index("orange")) # index of given item

# more_fruits = ["grape", "kiwi"]   # add multiple items
# fruits.extend(more_fruits)        # extend list
# print(fruits)

# fruits_copy = fruits.copy()       # copy list
# print(fruits_copy)

# joined_fruits = ", ".join(fruits) # join list items into a string
# print(joined_fruits)

# sliced_fruits = fruits[1:4]       # slice list
# print(sliced_fruits)

# print(min(num))                   # print minimum value in list

# print(max(num))                   # print maximum value in list

# print(sum([1, 2, 3, 4, 5]))       # print sum of all items in list


# Slicing: 
# fruits = ["applwsse", "banana", "orange", "mango", "apple"]

# print(fruits[1:4])
# print(fruits[:4])
# print(fruits[1:])
# print(fruits[0:5:2])
# print(fruits[::-2])
# print(fruits[::2])



#### taking lst from user

# lst = []
# n = int(input("Enter the size of list: "))
# print("Enter data: ")
# for i in range(n):
#     data = int(input("Data: "))
#     lst.append(data)
# print(lst)


### Searching:
# fruits = ["kiwi", "banana", "orange", "mango", "apple", "cherry"]
# target = input("Enter search target: ").lower()
# for i in fruits:
#     if i == target:
#         print(f"Found {target} at {fruits.index(i)} index")
#     else:
#             print("Not found")

### Good way
fruits = ["kiwi", "banana", "orange", "mango", "apple", "cherry"]

target = input("Enter search target: ").lower()

if target in fruits:
    print(f"Found {target} at index {fruits.index(target)}")
else:
    print("Not found")


# Tuple: it is a collection of items which is ordered, unchangeable(immutable), and allows duplicate values