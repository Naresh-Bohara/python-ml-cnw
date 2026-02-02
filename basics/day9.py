# Dicttionary: collection of data in key:value pair.
'''
syntax:
dict_name = {
        key1: value1
        key2: value2
        key3: value3
        .............
        .............
        .............
        keyn: valuen
}
'''

# Example: 
# student = {
#     "name": "Naresh Bohara",
#     "age": 23,
#     "city": "Dhangadhi"
# }
# print(student)

"""
Properties:
- mutable
key value pair
keys are unique
values can be duplicate
unordered
"""

## Accessing values:
# student = {
#     "name": "Naresh",
#     "age": 23,
#     "city": "Dhangadhi"
# }

# print(student["name"])
# print(student["age"])
# print(student["city"])


## using get method:
# print(student.get("name"))

## Looping through dictionaries:
# student = {
#     "name": "Naresh",
#     "age": 23,
#     "city": "Dhangadhi"
# }

# looping through key:
# for k in student:
#     print(k)

# looping through value:
# for v in student.values():
#     print(v)

# both 
# for k, v in student.items():
#     print(k,v)

### Methods in dictionary:
'''
get(): accessing values using key
keys(): return all the keys in dict
values(): return all the values in dict
items(): return key-value pair
update(): add new data or update existing data
pop(): remove using key
popitem(): remove last item
clear(): remove all data
copy(): create copy a dictionary
fromkey(): create dictionary with keys
'''

student = {
    "name": "Naresh",
    "age": 23,
    "city": "Dhangadhi"
}
# print(student.get("name"))
# print(student.keys())
# print(student.values())

# for k, v in student.items():
#     print(k,v)

## update existing dictionary:
student.update({"age": 25})
print(student)

# insert / add new data 
student.update({"rollno": 3})
print(student)
print()

# student.pop("age")
# print(student)

# student.popitem()
# print(student)

# student.clear()
# print(student)

# student_copy = student.copy()
# print(student_copy)

keys = ["name", "age", "city"]
student = dict.fromkeys(keys, "Unknown")
print(student)

# d = {}

# n = int(input("How many data? "))
# for i in range(1, n+1):
#     name = input("Enter name: ")
#     age = int(input("Enter age: "))
#     d[name] = age
# print(d)

# converting list -> dictionary
ls = [
    ["ram", 30],
    ["hari", 24],
    ["rohan", 21],
]
print(dict(ls))

## Searching:
d ={
    "name": ["Ram", "Shyam", "Hari"],
    "age": [22, 23, 24],
    "address": ["ktm", "dhangadhi", "pokhara"]
}

found=False
for i in d["name"]:
    if i.lower()=="shyam":
        print("Found")
        found=True
    
if not found:
    print("Not found")



### Nested Dictionaries
student = {
    "personal_info": {
        "name": "Naresh",
        "age": 23,
        "city": "Dhangadhi"
    },
    "academic_info": {
        "grade": "A+",
        "gpa": 3.8,
        "year": 3
    },
    "contact_info": {
        "email": "naresh@example.com",
        "phone": "9801234567"
    }
}

# print(student["personal_info"]) 
# print(student["academic_info"])


# Accessing nested values
# print(student["personal_info"]["name"])  # Naresh
# print(student["academic_info"]["gpa"])  # 3.8
# print(student["contact_info"]["email"])  # naresh@example.com