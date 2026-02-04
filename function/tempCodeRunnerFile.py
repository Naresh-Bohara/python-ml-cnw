# students = {
#     "student1": {"name": "ram", "age": 12},
#     "student2": {"name": "hari", "age": 20},
#     "student3": {"name": "shyam", "age": 23}
# }

# # Just like your k, v example but nested
# for k1, v1 in students.items():  # First level: student1, student2, etc.
#     print(f"\nOuter Key: {k1}")
#     print(f"Outer Value (full dict): {v1}")
    
#     for k2, v2 in v1.items():  # Second level: name, age
#         print(f"{k2}: {v2}")