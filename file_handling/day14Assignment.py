# file_path = "file_handling/hello.txt"
# with open(file_path, 'r') as file:
#     data = file.read()
#     print(data)

# target = input("Enter the word to remove from the file: ").strip()
# if target in data:
#     print(f"'{target}' found in the file.")
#     data = data.replace(target, "")
#     with open(file_path, 'w') as file:
#         file.write(data)
#     print(f"'{target}' has been removed from the file.")
# else:
#     print(f"'{target}' not found in the file.")


file_path = "file_handling/hello.txt"
target = input("Please enter the name of student: ").strip().title()

with open(file_path, 'r') as file:
    data = file.readlines()

with open(file_path, 'w') as file:
    found = False
    for line in data:
        if line.startswith(target + " "):
            found = True
            continue
        file.write(line)
if found:
    print("Deleted")
else:
    print("Not found.")