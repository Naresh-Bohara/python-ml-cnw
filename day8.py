# Tuple : It is a collection of data which is ordered and immutable (can't be changed once declared)

# t = (10, 20, 30, 40)
# print(t)
# print(type(t))

# t2 =(1, 2, "Naresh", 2.3)
# print(t2)

# Tuple with single element:
# t3 = ("tuple",)
# print(type(t3))


#  indexing in tuple:
# color = ("red", "yellow", "green", "pink", "purple", "white")
# print(color[2])
# print(color[1:4])
# print(color[:3])
# print(color[2:])
# print(color[::-1])


## Tuple is immutable
# color[2] = "brown"           # in tuple it can't be changed
# print(color[2])

# lis = [123,232,"rosh", 2, 2, 2, 2, 2, 2]
# lis[2] = "green"                # in list it can be changed
# print(lis)
# print(lis.count(2))

### Methods in tuple:
# t4 = (1, 2, 3, 4, 5, 1, 5, 3, 5, 66,6, 1, 1, 1)
# print(t4.count(1))
# print(t4.index(1))


# colors = ("red", "yellow", "green", "pink", "purple", "white")

# for color in colors:
#     print(color, end=" ")
# print()
# print(len(colors))


### Operations in tuple:
# t1 = (1, 2, 3, 4)
# t2 = (1, 2, 3, 4)

# concatination
# print(t1+t2)

# repetation
# print(t1*2)

# membership:
# print(2 in t2)          # True
# print(100 in t2)        # False

# Unpacking:
# a, b, c, d = t1
# print(a, b, c, d)

# In list:
# ls = [1, 13]
# x, y = ls
# print(x, y)


### Converting list to tuple and vice versa:
# converting list to tuple:
# lst = [1,2,3,4]
# print(type(lst))

# t = tuple(lst)
# print(t)
# print(type(t))

# # converting tuple to list:
# ls = list(t)
# print(ls)
# print(type(ls))


### Set:
"""
- collection of unordered elements
- unordered (indexing is not possible)
- mutable (can be changed)
- written using {}
"""
# s = {10, 20, 30, 40}
# print(type(s))
# print(s)

# # accessing set element
# for i in s:
#     print(i)

# # checking if element exist or not in set:
# if 20 in s:
#     print("yes 20 exist")
# else:
#     print("No it doesn't exist")

# ### Methods of set:
# numbers = {1, 2, 3, 4, 100, 12}
# # add(): add new element in set 
# numbers.add(2020)
# print(numbers)

# # update():
# numbers.update([1, 22,3, 0, 1, 2])
# print(numbers)

# # remove():
# numbers.remove(12)
# print(numbers)

# # discard():
# numbers.discard(1)
# print(numbers)

# pop(): remove random number
set2 = {2, 3, 4, 5}
set2.pop()
print(set2)

# # clear():
# set2.clear()
# print(set2)

### set operations:
# union()
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a.union(b))
# print(a | b)

# intersection
# print(a.intersection(b))
# print(a & b)

# # difference
# print(a.difference(b))
# print(a - b)

# # issubset()
# print(a.issubset(b))

# # issuperset()
# print(b.issuperset(a))

# # isdisjoint()
# print(b.isdisjoint(a))
