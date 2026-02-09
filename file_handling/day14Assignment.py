with open('file_handling/hello.txt', 'r') as file:
    data = file.read()
    print(data)

target = input("Enter the word to remove from the file: ").strip()
if target.lower() in data.lower():
    print(f"'{target}' found in the file.")
    data = data.replace(target, "")
    with open('file_handling/hello.txt', 'w') as file:
        file.write(data)
else:
    print(f"'{target}' not found in the file.")