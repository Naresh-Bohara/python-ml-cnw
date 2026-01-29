### --------------------- COMPLETE LIST COMPREHENSION ------------------------


# =========================================================
# LIST COMPREHENSION – SYNTAX TABLE
# =========================================================
# Type          | Syntax Pattern                                   | When to Use
# ------------- | -----------------------------------------------  | -------------------------------
# Basic         | [expression for item in iterable]                | Transform each item
# Filter        | [exp for item in iterable if condition]          | Keep only some items
# If-Else       | [val1 if cond else val2 for item in iterable]    | Choose value based on condition
# Nested        | [exp for item1 in iter1 for item2 in iter2]      | Cartesian product
# Nested Lists  | [exp for sublist in list for item in sublist]    | Flatten 2D lists
# =========================================================


# 1. BASIC FORM - TRANSFORMATION
# Rule: Apply operation to every element

# Square each number
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]  # [1, 4, 9, 16]
print(squares)

# Convert to uppercase
words = ["hi", "bye", "hello"]
upper = [w.upper() for w in words]  # ['HI', 'BYE', 'HELLO']
print(upper)

# Apply any function
names = ["Naresh", "Hem", "Santosh"]
lengths = [len(name) for name in names]  # [6, 3, 7]
print(lengths)


# 2. FILTERING - WITH if CONDITION
# Rule: Only include items that satisfy condition
# The if condition comes AFTER the for loop

# Get even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [n for n in numbers if n % 2 == 0]  # [2, 4, 6, 8]
print(evens)

# Words starting with 'a'
words = ["apple", "banana", "avocado", "cherry", "apricot"]
a_words = [w for w in words if w.startswith('a')]  # ['apple', 'avocado', 'apricot']
print(a_words)

# Multiple conditions
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
selected = [n for n in nums if n > 3 and n < 8]  # [4, 5, 6, 7]
print(selected)



# 3. IF-ELSE (CONDITIONAL EXPRESSIONS) 
# RULE: When using if-else, it goes BEFORE the for loop

# Mark numbers as even/odd
numbers = [1, 2, 3, 4, 5]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(labels)       # ['odd', 'even', 'odd', 'even', 'odd']

# Square only even numbers, keep odd as is
nums = [1, 2, 3, 4, 5]
result = [n**2 if n % 2 == 0 else n for n in nums]
print(result)       # [1, 4, 3, 16, 5]

# Grade classification
scores = [85, 42, 76, 91, 33]
grades = ["A" if s >= 90 else "B" if s >= 80 else "C" if s >= 70 else "F" for s in scores]
print(grades)       # ['B', 'F', 'C', 'A', 'F']


# # ❌ WRONG - if-else after for
# wrong = [n if n % 2 == 0 for n in range(5)]

# # ✅ CORRECT - if-else before for
# correct = ["even" if n % 2 == 0 else "odd" for n in range(5)]



# 4. FILTERING + TRANSFORMATION COMBINED
# Rule: Transform only filtered items

# Square only positive numbers
numbers = [-5, 3, -2, 8, -1, 4]
result = [n**2 for n in numbers if n > 0]  # [9, 64, 16]
print(result)

# Uppercase only long words
words = ["I", "love", "Python", "programming", "a", "lot"]
long_upper = [w.upper() for w in words if len(w) > 3]  # ['PYTHON', 'PROGRAMMING']
print(long_upper)


# 5. NESTED LOOPS - CARTESIAN PRODUCT
#  Rule: Outer loop first, then inner loop

# Generate all pairs
colors = ["red", "green"]
sizes = ["S", "M", "L"]
combinations = [(color, size) for color in colors for size in sizes]
print(combinations)      # [('red', 'S'), ('red', 'M'), ('red', 'L'), 
                         #  ('green', 'S'), ('green', 'M'), ('green', 'L')]

# Multiplication table
table = [f"{i} x {j} = {i*j}" for i in range(1, 4) for j in range(1, 4)]
print(table)
# ['1 x 1 = 1', '1 x 2 = 2', '1 x 3 = 3',
#  '2 x 1 = 2', '2 x 2 = 4', '2 x 3 = 6',
#  '3 x 1 = 3', '3 x 2 = 6', '3 x 3 = 9']


# 6. FLATTENING NESTED LISTS
# Rule: Use for sublist in list for item in sublist

# Flatten 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(flat)

# Extract numbers from mixed list
data = [[1, 2], "hello", [3, 4, 5], "world"]
numbers = [num for item in data if isinstance(item, list) for num in item]
print(numbers)        # [1, 2, 3, 4, 5]

# 7. DICTIONARY & SET COMPREHENSIONS
# Similar syntax, different brackets

# Dictionary Comprehension
squares_dict = {n: n**2 for n in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares_dict)

# Set Comprehension (removes duplicates)
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {n**2 for n in numbers}  # {1, 4, 9, 16}
print(unique_squares)


# REAL-WORLD EXAMPLES
# Example 1: Data Processing
# Clean data: remove None, convert to int
data = ["10", "20", None, "30", "", "40"]
clean = [int(x) for x in data if x and x.isdigit()]  # [10, 20, 30, 40]

# Example 2: File Processing
# Read and process lines
lines = ["  hello  ", "  world  ", "", "  python  "]
clean_lines = [line.strip() for line in lines if line.strip()]
print(clean_lines)        # ['hello', 'world', 'python']

# Example 3: Matrix Operations
# Transpose matrix
matrix = [[1, 2, 3], [4, 5, 6]]
transpose = [[row[i] for row in matrix] for i in range(3)]
print(transpose)            # [[1, 4], [2, 5], [3, 6]]



# PERFORMANCE TIPS
#  Use for: Simple transformations, filtering, readability
#  Use for: Small to medium datasets
#  Avoid for: Very complex logic (use regular loops)
#  Avoid for: Side effects (like printing inside)


# Readability Tip:
# For complex comprehensions, break into multiple lines:

# result = [
#     student.name.upper()
#     for student in students
#     if student.grade >= 80
#     and student.attendance > 90
# ]



# --------------------------------FINAL MASTER TEMPLATE------------------------------
new_list = [
    # 1. TRANSFORM/CONDITIONAL VALUE
    (transform_expression if condition else other_value)
    
    # 2. LOOP(S)
    for item in iterable
    for subitem in item  # if nested
    
    # 3. FILTER CONDITIONS
    if filter_condition
    and another_condition
    or optional_condition
]